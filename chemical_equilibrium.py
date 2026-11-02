import math


def main() -> None:
    raw_kc = input("Enter a positive value for Kc: ")
    print("Raw input data type:", type(raw_kc).__name__)

    try:
        kc = float(raw_kc)
    except ValueError:
        print("Error: Kc must be a valid number.")
        return

    print("Converted value data type:", type(kc).__name__)

    if not math.isfinite(kc):
        print("Error: Kc must be a finite number.")
        return

    if kc <= 0:
        print("Error: Kc must be greater than zero.")
        return

    # Kc*x^2 - (3*Kc + 1)x + 2*Kc = 0
    a = kc
    b = -(3 * kc + 1)
    c = 2 * kc

    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        print("Error: The quadratic equation has no real roots.")
        return

    if math.isclose(discriminant, 0.0, rel_tol=1e-12, abs_tol=1e-12):
        roots = [-b / (2 * a)]
    else:
        square_root = math.sqrt(discriminant)
        roots = [
            (-b + square_root) / (2 * a),
            (-b - square_root) / (2 * a),
        ]

    print("Quadratic coefficients:", f"a={a}", f"b={b}", f"c={c}")
    print("Discriminant:", discriminant)
    print("Roots:", roots)

    physical_roots = [
        root for root in roots
        if 0 <= root <= 1
    ]

    if not physical_roots:
        print("Error: No physically meaningful root exists between 0 and 1 mol/L.")
        return

    x = physical_roots[0]
    equilibrium_a = 2.0 - x
    equilibrium_b = 1.0 - x
    equilibrium_c = x

    print("Equilibrium concentrations:")
    print(f"[A] = {equilibrium_a:.3f} mol/L")
    print(f"[B] = {equilibrium_b:.3f} mol/L")
    print(f"[C] = {equilibrium_c:.3f} mol/L")


if __name__ == "__main__":
    main()
