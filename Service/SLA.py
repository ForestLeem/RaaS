from Service.Provider import Provider
from Service.Consumer import Consumer
from Service.QoS import QoS


class SLA:
    def __init__(self, _uid):
        self.uid = _uid
        self.provider = Provider()              # consist 1 provider
        self.consumer = Consumer()              # consist 1 consumer
        self.qos_list = []                      # consist QoS [0..*]

    def set_provider(self, _provider):
        # set SLA's provider
        if isinstance(_provider, Provider):
            self.provider = _provider

    def set_consumer(self, _consumer):
        # set SLA's consumer
        if isinstance(_consumer, Consumer):
            self.consumer = _consumer

    def add_qos(self, _qos):
        # add qos to service
        if isinstance(_qos, QoS):
            self.qos_list.append(_qos)

    def to_dict(self):
        result = {"idf": self.idf, "provider": self.provider.to_dict(), "consumer": self.consumer.to_dict()}

        # qos class list -> qos dict list
        tmp_qos_list = []
        for tmp in self.qos_list:
            tmp_qos_list.append(tmp.to_dict())
        result["qos"] = tmp_qos_list

        return result
