from abc import abstractmethod, ABC


class NotificationService(ABC):

    @abstractmethod
    def notify_town_crier(self, message):
        pass
