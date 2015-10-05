import appier
import appier_extras

class User(appier_extras.admin.Base):

    key = appier.field(
        type = unicode,
        index = True
    )