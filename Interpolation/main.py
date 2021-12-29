from sympy.abc import I
from utils.helpers import load_config
from inverse_interpolation import InverseInterpolation
from sympy import init_printing, init_session, pretty_print, latex, simplify

init_printing()

config = load_config('config.yml')
print(config)

client = InverseInterpolation(config)

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

client.fit(x, y)
for _x in x:
    print(client.eval(_x))

print(latex(simplify(client.res)))
