import appier
import appier_extras
from .category import Category

class Product(appier_extras.admin.Base):

    name = appier.field(
        type = unicode,
        index = True
    )

    size = appier.field(
        type = unicode,
        index = True
    )

    price = appier.field(
        type = float,
        index = True
    )

    image_url = appier.field(
        type = unicode,
        index = True
    )

    image_urls = appier.field(
        type = list
    )

    category = appier.field(
        type = appier.reference(
            Category
        )
    )
