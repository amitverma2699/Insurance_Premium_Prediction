import os
from pathlib import Path

package_name="InsurancePremiumPrediction"

list_of_files =[

    "github/workflows/.gitkeep",
    "source/__init__.py",
    "source/components/__init__.py",
    "source/components/data_ingestion.py",
    "source/components/data_transformation.py",
    "source/components/model_trainer.py",
    "source/pipelines/__init__.py",
    "source/pipelines/training_pipeline.py",
    "source/pipelines/prediction_pipeline.py",
    "source/logger.py",
    "source/exception.py",
    "source/utils/__init__.py",
    "source/utils/utils.py",
    "templates",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "setup.py",
    "app.py",
    "init_setup.sh"

]


# Create a Directory

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass

    else:
        print("File already exists")

