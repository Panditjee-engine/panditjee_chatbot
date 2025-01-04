import json

from immanuel.classes.serialize import ToJSON
from immanuel import charts


native = charts.Subject(
        date_time='2001-10-25 07:37',
        latitude='28.534491880873553',
        longitude='77.25222412700371'
    )

natal = charts.Natal(native)

print(json.dumps(natal.objects, cls=ToJSON, indent=4))