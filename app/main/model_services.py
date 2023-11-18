
from ..models import User, Reservation, Table, Role


def get_is_admin(active_user):
    """
    Get if active user is admin

    Parameters
    ----------
    active_user : User
        Active user in the app

    Returns
    -------
        bool
    """
    admin_role = Role.query.filter_by(name="Admin").first()
    is_admin = active_user.role == admin_role

    return is_admin
