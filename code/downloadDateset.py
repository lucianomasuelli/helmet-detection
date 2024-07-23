import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset(
    "open-images-v7",
    split="validation",
    label_types=["segmentations", "classifications"],
    classes = ["Motorcycle"],
    max_samples=100,
    seed=51,
    shuffle=True,
    dataset_name="motorcycle",
)