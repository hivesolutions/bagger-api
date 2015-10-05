import appier
import appier_extras

class Bag(appier_extras.admin.Base):

    user = appier.field(
        type = appier.reference(
            "User",
            name = "key"
        )
    )