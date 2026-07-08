class Roles:
    ADMIN = "ADMIN"
    USER = "USER"
    OWNER = "OWNER"


class Status:
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    PENDING = "PENDING"
    DELETED = "DELETED"


class ConversationType:
    CHAT = 'CHAT'
    EMAIL = 'EMAIL'
    VOICE = 'VOICE'


class AIProvider:
    OPENAI = 'OPENAI'
    CLAUDE = 'CLAUDE'
    GEMINI = 'GEMINI'


class OrganizationType:
    CLINIC = 'CLINIC'
    LAW = 'LAW'
    HR = 'HR'
    RETAIL = 'RETAIL'


roles = Roles
status = Status
conversationtype = ConversationType
aiProvider = AIProvider
organizationType = OrganizationType
