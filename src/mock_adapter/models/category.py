import appier
import appier_extras

class Category(appier_extras.admin.Base):

    name = appier.field(
        type = unicode,
        index = True
    )

    image_url = appier.field(
        type = unicode,
        index = True
    )
