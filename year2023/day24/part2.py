from sympy import solve, Eq, symbols
from year2023.day24.common import parse


def run(data: list[str], is_test: bool):
    hailstones = parse(data)

    # hailstone position + time * hailstone velocity = rock position + time * rock velocity
    # time = (rock position - hailstone position) / (hailstone velocity - rock velocity)
    #
    # The above has to be valid for all axes at the same time x = y = z
    # (r_px - h_px) / (h_vx - t_vx) = (r_py - h_py) / (h_vy - t_vy) = (r_pz - h_pz) / (h_vz - t_vz)
    #
    # It seems Sympy has issues with simplification when we have division in it due to possible zeros in denominator,
    # and we should change it to: (r_px - h_px) * (h_vy - t_vy) = (r_py - h_py) * (h_vx - t_vx) etc.
    r_px, r_py, r_pz, r_vx, r_vy, r_vz = symbols("r_px r_py r_pz r_vx r_vy r_vz")

    equations = []
    for hailstone in hailstones:
        h_px, h_py, h_pz = hailstone.position(0)
        h_vx, h_vy, h_vz = hailstone.velocity
        equations.append(Eq((r_px - h_px) * (h_vy - r_vy), (r_py - h_py) * (h_vx - r_vx)))
        equations.append(Eq((r_py - h_py) * (h_vz - r_vz), (r_pz - h_pz) * (h_vy - r_vy)))

        try:
            results = solve(equations)

            # We can get valid non-integer solutions as well, and we need to filter them out
            for result in results:
                if all(int(result[n]) == result[n] for n in [r_px, r_py, r_pz, r_vx, r_vy, r_vz]):
                    return int(result[r_px]) + int(result[r_py]) + int(result[r_pz])
        except:
            pass  # need more equations
