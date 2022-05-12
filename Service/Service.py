from Service.Provider import Provider
from Service.Operation import Operation
from Service.SLA import SLA
from Service.QoS import QoS


class Service:
    def __init__(self, _uid):
        self.context = "http://www.w3.org/ns/resource.jsonld"
        self.uid = _uid
        self.provider = Provider()              # consist 1 provider
        self.operation_list = []                # consist operation [1..*]
        self.sla_list = []                      # consist SLA [0..*]
        self.qos_list = []                      # consist QoS [0..*]

    def set_provider(self, _provider):
        # set service's provider
        if isinstance(_provider, Provider):
            self.provider = _provider

    def add_operation(self, _operation):
        # add operation to service
        if isinstance(_operation, Operation):
            self.operation_list.append(_operation)

    def add_sla(self, _sla):
        # add sla to service
        if isinstance(_sla, SLA):
            self.sla_list.append(_sla)

    def add_qos(self, _qos):
        # add qos to service
        if isinstance(_qos, QoS):
            self.qos_list.append(_qos)

    def to_dict(self):
        result = {"@context": self.context, "uid": self.uid, "provider": self.provider.to_dict()}

        # operation class list -> operation dict list
        tmp_operation_list = []
        for tmp in self.operation_list:
            tmp_operation_list.append(tmp.to_dict())
        result["operation"] = tmp_operation_list

        # sla class list -> sla dict list
        tmp_sla_list = []
        for tmp in self.sla_list:
            tmp_sla_list.append(tmp.to_dict())
        result["sla"] = tmp_sla_list

        # qos class list -> qos dict list
        tmp_qos_list = []
        for tmp in self.qos_list:
            tmp_qos_list.append(tmp.to_dict())
        result["qos"] = tmp_qos_list

        return result
