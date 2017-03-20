from .base import Base


class Soccer(Base):
    def __init__(self, API_KEY="05d52d8812a548c6a9f6f29ed60e8e00"):
        super(Soccer, self).__init__(API_KEY)
