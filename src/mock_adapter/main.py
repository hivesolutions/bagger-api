import appier
import appier_extras

import models

class BaggerApp(appier.WebApp):

    def __init__(self):
        appier.WebApp.__init__(
            self,
            session_c = appier.session.MemorySession,
            parts = (
                appier_extras.AdminPart,
            )
        )

BaggerApp().serve()
