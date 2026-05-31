import json
from datetime import datetime
from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "tickets.csv"
CLEAN_OUTPUT_FILE = BASE_DIR / "data" / "tickets_clean.csv"
FILTERED_OUTPUT_FILE = BASE_DIR / "data" / "critical_tickets.csv"
JSON_OUTPUT_FILE = BASE_DIR / "data" / "critical_tickets.json"

REQUIRED_COLUMNS = [
    "id",
    "titulo",
    "estado",
    "prioridad",
    "solicitante"
]


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

        # Normalización de nombres de columnas
        dataframe.columns = (
            dataframe.columns
            .str.strip()
            .str.normalize('NFKD')
            .str.encode('ascii', errors='ignore')
            .str.decode('utf-8')
            .str.replace(' ', '_')
            .str.lower()
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


def validate_required_columns(dataframe: pd.DataFrame) -> None:
    """
    Validate required columns existence.

    Args:
        dataframe (pd.DataFrame): Input dataframe.
    """

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )


def clean_ticket_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and normalize ticket dataset.

    Args:
        dataframe (pd.DataFrame): Raw dataframe.

    Returns:
        pd.DataFrame: Cleaned dataframe.
    """

    cleaned_df = dataframe.copy()

    # Remove extra spaces from string values
    for column in cleaned_df.select_dtypes(include="object"):
        cleaned_df[column] = (
            cleaned_df[column]
            .fillna("")
            .astype(str)
            .str.strip()
        )

    # Normalize critical fields
    cleaned_df["estado"] = (
        cleaned_df["estado"]
        .str.capitalize()
    )

    cleaned_df["prioridad"] = (
        cleaned_df["prioridad"]
        .str.capitalize()
    )

    # Remove duplicated tickets
    cleaned_df = cleaned_df.drop_duplicates(
        subset=["id"]
    )

    return cleaned_df


def filter_critical_tickets(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Filter critical pending tickets.

    Conditions:
    - estado = Pendiente
    - prioridad = Alta

    Args:
        dataframe (pd.DataFrame): Clean dataframe.

    Returns:
        pd.DataFrame: Filtered dataframe.
    """

    filtered_df = dataframe[
        (dataframe["estado"] == "Pendiente") &
        (dataframe["prioridad"] == "Alta")
    ].copy()

    return filtered_df


def export_to_csv(
    dataframe: pd.DataFrame,
    output_path: Path
) -> None:
    """
    Export dataframe to CSV file.

    Args:
        dataframe (pd.DataFrame): Dataframe to export.
        output_path (Path): Output file path.
    """

    dataframe.to_csv(
        output_path,
        sep=";",
        index=False,
        encoding="utf-8"
    )


def export_to_json(
    dataframe: pd.DataFrame,
    output_path: Path
) -> None:
    """
    Export filtered tickets to JSON format.

    Args:
        dataframe (pd.DataFrame): Filtered dataframe.
        output_path (Path): Output JSON file path.
    """
    # Remplazar NaN por None para que se serialice como null en JSON
    dataframe = dataframe.astype(object).where(
        pd.notnull(dataframe),
        None
    )

    payload = {
        "generated_at": (
            datetime.now().isoformat()
        ),
        "total_critical_tickets": len(dataframe),
        "tickets": dataframe.to_dict(
            orient="records"
        )
    }

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as json_file:

        json.dump(
            payload,
            json_file,
            indent=4,
            ensure_ascii=False
        )


def main() -> None:
    """
    Main execution flow.
    """

    try:
        # 1. Extracción
        tickets_df = load_tickets(DATA_FILE)
        validate_required_columns(tickets_df)

        # 2. Transformación y Limpieza
        cleaned_df = clean_ticket_data(tickets_df)
        export_to_csv(cleaned_df, CLEAN_OUTPUT_FILE)

        # 3. Lógica de Negocio (Filtrado)
        filtered_df = filter_critical_tickets(cleaned_df)
        export_to_csv(filtered_df, FILTERED_OUTPUT_FILE)
        export_to_json(filtered_df, JSON_OUTPUT_FILE)

        # 4. Reporte de ejecución
        print("\nTickets loaded and cleaned successfully.")
        print(f"Total records: {len(cleaned_df)}")
        print(
            f"Clean dataset exported to: "
            f"{CLEAN_OUTPUT_FILE}"
        )

        print(
            f"\nCritical pending tickets found: "
            f"{len(filtered_df)}"
        )
        print(
            f"Filtered dataset exported to: "
            f"{FILTERED_OUTPUT_FILE}"
        )
        print(
            f"JSON dataset exported to: "
            f"{JSON_OUTPUT_FILE}"
        )

        if filtered_df.empty:
            print(
                "\n[INFO] No critical pending tickets found."
            )

    except FileNotFoundError as error:
        print(f"\n[FILE ERROR] {error}")

    except ValueError as error:
        print(f"\n[VALIDATION ERROR] {error}")

    except Exception as error:
        print(f"\n[UNEXPECTED ERROR] {error}")


if __name__ == "__main__":
    main()