from ODRL import Party
from ODRL import Asset
from ODRL import Action
from ODRL import Constraint
from ODRL import Policy
from ODRL import Rule
from Service import Consumer
from Service import Operation
from Service import Provider
from Service import QoS
from Service import Service
from Service import SLA


def Asset2Service_c(_asset):
    # σ(ass: C.Asset) → ser: C.Service
    if isinstance(_asset, Asset.Asset):
        new_service = Service.Service(_asset.uid)
        return new_service


def Party2Provider_c(_party):
    # σ(ass: C.Party) → ser: C.Provider
    if isinstance(_party, Party.Party) and _party.function == "assigner":
        new_provider = Provider.Provider(_party.uid)
        return new_provider


def Party2Consumer_c(_party):
    # σ(ass: C.Party) → ser: C.Consumer
    if isinstance(_party, Party.Party) and _party.function == "assignee":
        new_consumer = Consumer.Consumer(_party.uid)
        return new_consumer


def Policy2SLA_c(_policy):
    # σ(ass: C.Policy) → ser: C.SLA
    if isinstance(_policy, Policy.Policy):
        new_SLA = SLA.SLA(_policy.uid)
        return new_SLA


def Rule2None_c(_rule):
    # σ(ass:C.Rule) → φ
    if isinstance(_rule, Rule.Rule):
        pass


def Action2Operation_c(_action):
    # σ(ass:C.Action) → ser:C.Operation
    if isinstance(_action, Action.Action):
        new_operation = Operation.Operation(_action.name)
        return new_operation


def Constraint2QoS_c(_constraint):
    # σ(ass:C.Constraint) → ser:C.QoS
    if isinstance(_constraint, Constraint.Constraint):
        new_QoS = QoS.QoS(_constraint.leftOperand, _constraint.rightOperand, _constraint.operator, _constraint.unit)
        return new_QoS


def Asset2Service(_policy):
    if isinstance(_policy, Policy.Policy):
        result_service_list = []
        # generate service for each asset
        for tmp_asset in _policy.asset_list:
            # σ(ass:R.asset(C.Policy,C.Asset)) → ser:R.sla(C.Service,C.SLA)
            tmp_service = Asset2Service_c(tmp_asset)
            tmp_sla = Policy2SLA_c(_policy)
            tmp_service.add_sla(tmp_sla)
            result_service_list.append(tmp_service)

        # update service
        for tmp_service in result_service_list:
            for tmp_party in _policy.party_list:
                # σ(ass:R.party(C.Policy,C.Party)) → ser:R.provider(C.SLA,C.Provider) ∪
                # ser:R.provider(C.Service,C.Provider)
                if tmp_party.function == "assigner":
                    tmp_provider = Party2Provider_c(tmp_party)
                    tmp_service.provider = tmp_provider
                    # add provider for each sla in service
                    for tmp_sla in tmp_service.sla_list:
                        tmp_sla.setProvider(tmp_provider)
                if tmp_party.function == "assignee":
                    # SLA.consumer ← Consumer
                    tmp_consumer = Party2Consumer_c(tmp_party)
                    # add consumer for each sla in service
                    for tmp_sla in tmp_service.sla_list:
                        tmp_sla.set_consumer(tmp_consumer)
            for tmp_action in _policy.action:
                # Service.operation ← Operation
                tmp_operation = Action2Operation_c(tmp_action)
                tmp_service.add_operation(tmp_operation)
            for tmp_constraint in



