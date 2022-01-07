from sympy import latex, simplify

from inverse_interpolation import InverseInterpolation
from utils.helpers import load_config

config = load_config('config.yml')

client = InverseInterpolation(config)

x = [1, 2, 3, 4, 5]

y = [1, 4, 9, 16, 25]
client.fit(x, y)
for _x in x:
    print(client.eval(_x))

print(latex(simplify(client.res)))
