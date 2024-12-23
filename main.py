from src.services.GupyService import GupyService


if __name__ == "__main__":
        filter_labels = [
            "analista",
            "dados",
            "python",
            "data",
            "Desenvolvedor",
            "Dev",
            "Front",
            "Back",
            "Full Stack",
            "FullStack",
            "Software",
            "DevOps",
            "Business Intelligence",
            "Machine Learning",
            "Inteligência Artificial",
        ]

        labels = GupyService(filter_labels)
        labels.get_and_save_to_json()