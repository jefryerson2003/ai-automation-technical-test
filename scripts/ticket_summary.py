from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent.parent
JSON_FILE = BASE_DIR / "data" / "critical_tickets.json"


def load_ticket_summary(file_path: Path) -> dict:
    """
    Load critical tickets JSON file.

    Args:
        file_path (Path): Path to JSON file.

    Returns:
        dict: Parsed JSON content.
    """

    if not file_path.exists():
        raise FileNotFoundError(
            f"JSON file not found: {file_path}"
        )

    try:
        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as json_file:

            data = json.load(json_file)

            return data

    except json.JSONDecodeError:
        raise ValueError(
            "The JSON file is corrupted or invalid."
        )


def generate_summary(data: dict) -> str:
    """
    Generate conversational summary
    from critical tickets data.

    Args:
        data (dict): JSON payload.

    Returns:
        str: Human-readable summary.
    """

    total_tickets = data.get(
        "total_critical_tickets",
        0
    )

    if total_tickets == 0:
        return (
            "Actualmente no tienes "
            "tickets críticos pendientes."
        )

    return (
        f"Actualmente tienes "
        f"{total_tickets} tickets críticos "
        f"pendientes por resolver."
    )


def main() -> None:
    """
    Main execution flow.
    """

    try:
        ticket_data = load_ticket_summary(
            JSON_FILE
        )

        summary = generate_summary(
            ticket_data
        )

        print("\nTicket Summary")
        print("-" * 40)
        print(summary)

    except FileNotFoundError as error:
        print(f"\n[FILE ERROR] {error}")

    except ValueError as error:
        print(f"\n[DATA ERROR] {error}")

    except Exception as error:
        print(f"\n[UNEXPECTED ERROR] {error}")


if __name__ == "__main__":
    main()