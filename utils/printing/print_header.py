def print_header_with_stars(message: str, no_of_stars: int = 8) -> None:
    print(f"{message:*^{len(message) + no_of_stars}}")
