from datetime import datetime
import json
import os
import requests


class GupyService:
    def __init__(self, search_labels):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition std-1)"
        }
        self.search_labels = search_labels
        self.ids = set()
        self.folder = "src/data/vacancies"
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.archive_name = f"result_{timestamp}.json"
        self.complete_path = os.path.join(self.folder, self.archive_name)
        
        os.makedirs(self.folder, exist_ok=True)

    def _get(self, label):
        try:
            url = f"https://portal.api.gupy.io/api/job?name={label}&offset=0&limit=400"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao fazer a requisição para {url}: {e}")
            raise

    def get_and_save_to_json(self):
        try:
            all_data = []
            
            for label in self.search_labels:
                print(f"Buscando vagas para: {label}")
                data = self._get(label)
                all_data.append({label: data})
            
            with open(self.complete_path, "w", encoding="utf-8") as json_file:
                json.dump(all_data, json_file, indent=4, ensure_ascii=False)
                print(f"Dados salvos com sucesso no arquivo '{self.complete_path}'.")
        
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
        
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar o JSON: {e}")
