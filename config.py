from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "AgF2ky8AjSzO6Wbk5lzM3wXSPdcFm7p0pcupRNkmOdmweQGt15jlGgWAWkNvys3ddjLU-IpPilm-LOpc1qJx07N4wFmgvyt46BSpguHnxRhoyzBNWZeJx47v1c1rAJzCIMNAUgpdfA308oC-xA3Z6SQxvx7HMmeMjOiHf-pxrvPQpr9paB0hDlPHpUookO6xO_8b4quOOT-EUnGRIs70-998l0xIRzoQsqNoFcNv2VGq6jy98l8xsUA7ThEJPnaeMTrxI-5I_4fBQ9FBrA0IbdUpCYPubwf_jqCk17nFLf2edZh1KLQ6w0mXaDXXvrHbvZQd5cKl0vWbhI_QDGwS8ILGs7YyoAAAAAGLGQbjAA")
BOT_TOKEN = getenv("BOT_TOKEN", "7356145623:AAEfeB8yGbQMd_CIeAuMGUQalj6gob7MSXI")
BOT_USERNAME = getenv("BOT_USERNAME", "NezrinNmusicRobot")
admins = {}
API_ID = int(getenv("API_ID", "24548143"))
API_HASH = getenv("API_HASH", "6cba049c135a0393615878ea1e3c9443")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6634423600").split()))
