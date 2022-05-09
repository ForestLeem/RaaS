from ODRL import Party
from ODRL import Asset
from ODRL import Action
from ODRL import Constraint
from ODRL import Policy
from ODRL import Rule
from Resource import Provider
from Resource import Resource as Res
from Resource import Interface
from Resource import Func_Char
from Resource import Non_Func_Char
from Resource import Operation


def Provider2Party_c(_provider):
    # σ(res: C.Provider) → ass: C.Party
    if isinstance(_provider, Provider.Provider):
        new_party = Party.Party("assigner", _provider.uid)
        return new_party


def Resource2None_c(_resource):
    # σ(res:C.Resource) → φ
    if isinstance(_resource, Res.Resource):
        pass


def Interface2Asset_c(_interface):
    # σ(res:C.Interface) → ass:C.Asset
    if isinstance(_interface, Interface.Interface):
        new_asset = Asset.Asset("target", _interface.uid)
        return new_asset


def Operation2Action_c(_operation):
    if isinstance(_operation, Operation.Operation):
        new_action = Action.Action()
        new_action.name = _operation.uid        # default is operation uid (may change to ODRL vocab)
        return new_action


def Func_Char2None_c(_func_char):
    if isinstance(_func_char, Func_Char.FnChar):
        pass


def Non_Func_Char2Constraint_c(_non_func_char, _type):
    if isinstance(_non_func_char, Non_Func_Char.NonFnChar):
        new_constraint = Constraint.Constraint(_type)
        new_constraint.leftOperand = "any uid(need to setting)"               # need to be setting
        new_constraint.operator = ""                        # need to be setting
        new_constraint.rightOperand = _non_func_char.value
        new_constraint.unit = _non_func_char.dataType
        return new_constraint


def Resource2Asset(_resource):
    if isinstance(_resource, Res.Resource):
        #
        asset_result_list = []

        # σ(res: C.Provider) → ass: C.Party
        ass_party = Provider2Party_c(_resource.provider)

        # σ(res: C.Resource) → φ

        # σ(res:C.Interface) → ass:C.Asset
        # 1 resource may have 1 or more interfaces
        interface_to_asset = {}
        for tmp_interface in _resource.interface_list:
            # σ(res:R.operation(C.Interface,C.Operation)) →
            # ass:R.action(C.Rule,C.Action) ∪ ass:R.asset(C.Rule,C.Asset)

            # interface -> asset
            tmp_rule_list = []

            # one rule must have one action
            for tmp_operation in tmp_interface.operation_list:
                # rule
                tmp_rule = Rule.Rule("permission")  # default

                # σ(res:C.Operation) → ass:C.Action
                tmp_action = Operation2Action_c(tmp_operation)
                tmp_rule.action = tmp_action

                # σ(res:R.non_functional_char(C.Operation,C.Non Functional Characteristic)) →
                # ass:R.refinement(C.Action,C.Constraint)
                for tmp_non_char in tmp_operation.NonFnChar_list:
                    tmp_refinement = Non_Func_Char2Constraint_c(tmp_non_char, "refinement")
                    tmp_action.add_refinement(tmp_refinement)

                # σ(res:R.non functional char(C.Interface,C.Non Functional Characteristic)) →
                # ass:R.constraint(C.Rule,C.Constraint) ∪ ass:R.asset(C.Rule,C.Asset)
                tmp_asset = Interface2Asset_c(tmp_interface)
                tmp_rule.add_asset(tmp_asset)
                for tmp_non_char in tmp_interface.NonFnChar_list:
                    tmp_constraint = Non_Func_Char2Constraint_c(tmp_non_char, "constraint")
                    tmp_rule.add_constraint(tmp_constraint)

                tmp_rule_list.append(tmp_rule)

            interface_to_asset[tmp_interface] = tmp_rule_list

        result_policy = []
        for tmp in _resource.interface_list:
            tmp_rule = interface_to_asset[tmp]

            # Policy.asset ← Asset
            tmp_policy = Policy.Policy("Agreement", "http://example.com/policy:01")
            tmp_policy.add_asset(Interface2Asset_c(tmp))

            # Policy.party ← Party
            tmp_policy.add_party(Provider2Party_c(_resource.provider))

            # permission
            for tmp_r in tmp_rule:
                tmp_policy.add_permission(tmp_r)

        return result_policy




