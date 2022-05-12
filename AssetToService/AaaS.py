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


def Asset2Service(_asset):
    if isinstance(_asset, Asset.Asset):


