from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "tickets.csv"


def load_tickets(file_path: Path) -> pd.DataFrame:
    """
    Load tickets dataset from CSV file.

    Args:
        file_path (Path): Path to CSV file.

    Returns:
        pd.DataFrame: Loaded dataframe.
    """

    if not file_path.exists():
        raise FileNotFoundError(
            f"Input file not found: {file_path}"
        )

    try:
        dataframe = pd.read_csv(
            file_path,
            sep=";",
            encoding="utf-8"
        )

        return dataframe

    except pd.errors.EmptyDataError:
        raise ValueError(
            "The input file is empty."
        )

    except pd.errors.ParserError:
        raise ValueError(
            "The input file is corrupted or has invalid structure."
        )


def main() -> None:
    """
    Main execution flow.
    """

    try:
        tickets_df = load_tickets(DATA_FILE)

        print("\nTickets loaded successfully.")
        print(f"Total records: {len(tickets_df)}")

    except Exception as error:
        print(f"\n[ERROR] {error}")


if __name__ == "__main__":
    main()