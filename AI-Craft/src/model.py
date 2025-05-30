{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e1a02cf8-8941-48e2-85ee-d0c2a5a376eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: torch in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (2.6.0)\n",
      "Requirement already satisfied: transformers in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (4.49.0)\n",
      "Requirement already satisfied: datasets in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (3.3.2)\n",
      "Requirement already satisfied: accelerate in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (1.4.0)\n",
      "Requirement already satisfied: filelock in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from torch) (3.17.0)\n",
      "Requirement already satisfied: typing-extensions>=4.10.0 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from torch) (4.12.2)\n",
      "Requirement already satisfied: networkx in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from torch) (3.4.2)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from torch) (3.1.5)\n",
      "Requirement already satisfied: fsspec in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from torch) (2024.12.0)\n",
      "Requirement already satisfied: setuptools in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from torch) (75.8.2)\n",
      "Requirement already satisfied: sympy==1.13.1 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from torch) (1.13.1)\n",
      "Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from sympy==1.13.1->torch) (1.3.0)\n",
      "Requirement already satisfied: huggingface-hub<1.0,>=0.26.0 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from transformers) (0.29.1)\n",
      "Requirement already satisfied: numpy>=1.17 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from transformers) (2.2.3)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from transformers) (24.2)\n",
      "Requirement already satisfied: pyyaml>=5.1 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from transformers) (6.0.2)\n",
      "Requirement already satisfied: regex!=2019.12.17 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from transformers) (2024.11.6)\n",
      "Requirement already satisfied: requests in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from transformers) (2.32.3)\n",
      "Requirement already satisfied: tokenizers<0.22,>=0.21 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from transformers) (0.21.0)\n",
      "Requirement already satisfied: safetensors>=0.4.1 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from transformers) (0.5.3)\n",
      "Requirement already satisfied: tqdm>=4.27 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from transformers) (4.67.1)\n",
      "Requirement already satisfied: pyarrow>=15.0.0 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from datasets) (19.0.1)\n",
      "Requirement already satisfied: dill<0.3.9,>=0.3.0 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from datasets) (0.3.8)\n",
      "Requirement already satisfied: pandas in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from datasets) (2.2.3)\n",
      "Requirement already satisfied: xxhash in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from datasets) (3.5.0)\n",
      "Requirement already satisfied: multiprocess<0.70.17 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from datasets) (0.70.16)\n",
      "Requirement already satisfied: aiohttp in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from datasets) (3.11.13)\n",
      "Requirement already satisfied: psutil in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from accelerate) (7.0.0)\n",
      "Requirement already satisfied: aiohappyeyeballs>=2.3.0 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from aiohttp->datasets) (2.4.6)\n",
      "Requirement already satisfied: aiosignal>=1.1.2 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from aiohttp->datasets) (1.3.2)\n",
      "Requirement already satisfied: attrs>=17.3.0 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from aiohttp->datasets) (25.1.0)\n",
      "Requirement already satisfied: frozenlist>=1.1.1 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from aiohttp->datasets) (1.5.0)\n",
      "Requirement already satisfied: multidict<7.0,>=4.5 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from aiohttp->datasets) (6.1.0)\n",
      "Requirement already satisfied: propcache>=0.2.0 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from aiohttp->datasets) (0.3.0)\n",
      "Requirement already satisfied: yarl<2.0,>=1.17.0 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from aiohttp->datasets) (1.18.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from requests->transformers) (3.4.1)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from requests->transformers) (3.10)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from requests->transformers) (2.3.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from requests->transformers) (2025.1.31)\n",
      "Requirement already satisfied: colorama in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from tqdm>=4.27->transformers) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from jinja2->torch) (3.0.2)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from pandas->datasets) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from pandas->datasets) (2025.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from pandas->datasets) (2025.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\raunak saoji\\appdata\\roaming\\python\\python313\\site-packages (from python-dateutil>=2.8.2->pandas->datasets) (1.17.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install torch transformers datasets accelerate\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ea40143d-b8ae-4c78-85f4-069eb4c00e80",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DatasetDict({\n",
      "    train: Dataset({\n",
      "        features: ['Unnamed: 0', 'situation', 'emotion'],\n",
      "        num_rows: 19209\n",
      "    })\n",
      "    validation: Dataset({\n",
      "        features: ['Unnamed: 0', 'situation', 'emotion'],\n",
      "        num_rows: 2756\n",
      "    })\n",
      "    test: Dataset({\n",
      "        features: ['Unnamed: 0', 'situation', 'emotion'],\n",
      "        num_rows: 2542\n",
      "    })\n",
      "})\n",
      "{'Unnamed: 0': 0, 'situation': 'I remember going to the fireworks with my best friend. There was a lot of people, but it only felt like us in the world.', 'emotion': 'sentimental'}\n"
     ]
    }
   ],
   "source": [
    "from datasets import load_dataset\n",
    "\n",
    "# Load dataset\n",
    "ds = load_dataset(\"bdotloh/empathetic-dialogues-contexts\")\n",
    "\n",
    "# Check dataset structure\n",
    "print(ds)\n",
    "print(ds[\"train\"][0])  # See first sample\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "69c6d436-86b3-4910-9eaa-5b51bf78c5ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "def replace_joyful_with_happy(example):\n",
    "    if example[\"emotion\"] == \"joyful\":\n",
    "        example[\"emotion\"] = \"happy\"\n",
    "    return example\n",
    "\n",
    "# Apply modification\n",
    "ds = ds.map(replace_joyful_with_happy)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fc853506-bbc4-4a96-9b5b-8c21d5c3ad92",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "53117bfa6e79477196bd94f74317695a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Map:   0%|          | 0/19209 [00:00<?, ? examples/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "ename": "KeyError",
     "evalue": "'context'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[4]\u001b[39m\u001b[32m, line 7\u001b[39m\n\u001b[32m      4\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m example\n\u001b[32m      6\u001b[39m \u001b[38;5;66;03m# Apply modification\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m7\u001b[39m ds = \u001b[43mds\u001b[49m\u001b[43m.\u001b[49m\u001b[43mmap\u001b[49m\u001b[43m(\u001b[49m\u001b[43mreplace_in_text\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\dataset_dict.py:902\u001b[39m, in \u001b[36mDatasetDict.map\u001b[39m\u001b[34m(self, function, with_indices, with_rank, input_columns, batched, batch_size, drop_last_batch, remove_columns, keep_in_memory, load_from_cache_file, cache_file_names, writer_batch_size, features, disable_nullable, fn_kwargs, num_proc, desc)\u001b[39m\n\u001b[32m    898\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m cache_file_names \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[32m    899\u001b[39m     cache_file_names = {k: \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;28;01mfor\u001b[39;00m k \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mself\u001b[39m}\n\u001b[32m    900\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m DatasetDict(\n\u001b[32m    901\u001b[39m     {\n\u001b[32m--> \u001b[39m\u001b[32m902\u001b[39m         k: \u001b[43mdataset\u001b[49m\u001b[43m.\u001b[49m\u001b[43mmap\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m    903\u001b[39m \u001b[43m            \u001b[49m\u001b[43mfunction\u001b[49m\u001b[43m=\u001b[49m\u001b[43mfunction\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    904\u001b[39m \u001b[43m            \u001b[49m\u001b[43mwith_indices\u001b[49m\u001b[43m=\u001b[49m\u001b[43mwith_indices\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    905\u001b[39m \u001b[43m            \u001b[49m\u001b[43mwith_rank\u001b[49m\u001b[43m=\u001b[49m\u001b[43mwith_rank\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    906\u001b[39m \u001b[43m            \u001b[49m\u001b[43minput_columns\u001b[49m\u001b[43m=\u001b[49m\u001b[43minput_columns\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    907\u001b[39m \u001b[43m            \u001b[49m\u001b[43mbatched\u001b[49m\u001b[43m=\u001b[49m\u001b[43mbatched\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    908\u001b[39m \u001b[43m            \u001b[49m\u001b[43mbatch_size\u001b[49m\u001b[43m=\u001b[49m\u001b[43mbatch_size\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    909\u001b[39m \u001b[43m            \u001b[49m\u001b[43mdrop_last_batch\u001b[49m\u001b[43m=\u001b[49m\u001b[43mdrop_last_batch\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    910\u001b[39m \u001b[43m            \u001b[49m\u001b[43mremove_columns\u001b[49m\u001b[43m=\u001b[49m\u001b[43mremove_columns\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    911\u001b[39m \u001b[43m            \u001b[49m\u001b[43mkeep_in_memory\u001b[49m\u001b[43m=\u001b[49m\u001b[43mkeep_in_memory\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    912\u001b[39m \u001b[43m            \u001b[49m\u001b[43mload_from_cache_file\u001b[49m\u001b[43m=\u001b[49m\u001b[43mload_from_cache_file\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    913\u001b[39m \u001b[43m            \u001b[49m\u001b[43mcache_file_name\u001b[49m\u001b[43m=\u001b[49m\u001b[43mcache_file_names\u001b[49m\u001b[43m[\u001b[49m\u001b[43mk\u001b[49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    914\u001b[39m \u001b[43m            \u001b[49m\u001b[43mwriter_batch_size\u001b[49m\u001b[43m=\u001b[49m\u001b[43mwriter_batch_size\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    915\u001b[39m \u001b[43m            \u001b[49m\u001b[43mfeatures\u001b[49m\u001b[43m=\u001b[49m\u001b[43mfeatures\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    916\u001b[39m \u001b[43m            \u001b[49m\u001b[43mdisable_nullable\u001b[49m\u001b[43m=\u001b[49m\u001b[43mdisable_nullable\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    917\u001b[39m \u001b[43m            \u001b[49m\u001b[43mfn_kwargs\u001b[49m\u001b[43m=\u001b[49m\u001b[43mfn_kwargs\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    918\u001b[39m \u001b[43m            \u001b[49m\u001b[43mnum_proc\u001b[49m\u001b[43m=\u001b[49m\u001b[43mnum_proc\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    919\u001b[39m \u001b[43m            \u001b[49m\u001b[43mdesc\u001b[49m\u001b[43m=\u001b[49m\u001b[43mdesc\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    920\u001b[39m \u001b[43m        \u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    921\u001b[39m         \u001b[38;5;28;01mfor\u001b[39;00m k, dataset \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mself\u001b[39m.items()\n\u001b[32m    922\u001b[39m     }\n\u001b[32m    923\u001b[39m )\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\arrow_dataset.py:562\u001b[39m, in \u001b[36mtransmit_format.<locals>.wrapper\u001b[39m\u001b[34m(*args, **kwargs)\u001b[39m\n\u001b[32m    555\u001b[39m self_format = {\n\u001b[32m    556\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mtype\u001b[39m\u001b[33m\"\u001b[39m: \u001b[38;5;28mself\u001b[39m._format_type,\n\u001b[32m    557\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mformat_kwargs\u001b[39m\u001b[33m\"\u001b[39m: \u001b[38;5;28mself\u001b[39m._format_kwargs,\n\u001b[32m    558\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mcolumns\u001b[39m\u001b[33m\"\u001b[39m: \u001b[38;5;28mself\u001b[39m._format_columns,\n\u001b[32m    559\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33moutput_all_columns\u001b[39m\u001b[33m\"\u001b[39m: \u001b[38;5;28mself\u001b[39m._output_all_columns,\n\u001b[32m    560\u001b[39m }\n\u001b[32m    561\u001b[39m \u001b[38;5;66;03m# apply actual function\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m562\u001b[39m out: Union[\u001b[33m\"\u001b[39m\u001b[33mDataset\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33mDatasetDict\u001b[39m\u001b[33m\"\u001b[39m] = \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    563\u001b[39m datasets: List[\u001b[33m\"\u001b[39m\u001b[33mDataset\u001b[39m\u001b[33m\"\u001b[39m] = \u001b[38;5;28mlist\u001b[39m(out.values()) \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(out, \u001b[38;5;28mdict\u001b[39m) \u001b[38;5;28;01melse\u001b[39;00m [out]\n\u001b[32m    564\u001b[39m \u001b[38;5;66;03m# re-apply format to the output\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\arrow_dataset.py:3079\u001b[39m, in \u001b[36mDataset.map\u001b[39m\u001b[34m(self, function, with_indices, with_rank, input_columns, batched, batch_size, drop_last_batch, remove_columns, keep_in_memory, load_from_cache_file, cache_file_name, writer_batch_size, features, disable_nullable, fn_kwargs, num_proc, suffix_template, new_fingerprint, desc)\u001b[39m\n\u001b[32m   3073\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m transformed_dataset \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[32m   3074\u001b[39m     \u001b[38;5;28;01mwith\u001b[39;00m hf_tqdm(\n\u001b[32m   3075\u001b[39m         unit=\u001b[33m\"\u001b[39m\u001b[33m examples\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m   3076\u001b[39m         total=pbar_total,\n\u001b[32m   3077\u001b[39m         desc=desc \u001b[38;5;129;01mor\u001b[39;00m \u001b[33m\"\u001b[39m\u001b[33mMap\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m   3078\u001b[39m     ) \u001b[38;5;28;01mas\u001b[39;00m pbar:\n\u001b[32m-> \u001b[39m\u001b[32m3079\u001b[39m \u001b[43m        \u001b[49m\u001b[38;5;28;43;01mfor\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mrank\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mdone\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcontent\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;129;43;01min\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mDataset\u001b[49m\u001b[43m.\u001b[49m\u001b[43m_map_single\u001b[49m\u001b[43m(\u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mdataset_kwargs\u001b[49m\u001b[43m)\u001b[49m\u001b[43m:\u001b[49m\n\u001b[32m   3080\u001b[39m \u001b[43m            \u001b[49m\u001b[38;5;28;43;01mif\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mdone\u001b[49m\u001b[43m:\u001b[49m\n\u001b[32m   3081\u001b[39m \u001b[43m                \u001b[49m\u001b[43mshards_done\u001b[49m\u001b[43m \u001b[49m\u001b[43m+\u001b[49m\u001b[43m=\u001b[49m\u001b[43m \u001b[49m\u001b[32;43m1\u001b[39;49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\arrow_dataset.py:3495\u001b[39m, in \u001b[36mDataset._map_single\u001b[39m\u001b[34m(shard, function, with_indices, with_rank, input_columns, batched, batch_size, drop_last_batch, remove_columns, keep_in_memory, cache_file_name, writer_batch_size, features, disable_nullable, fn_kwargs, new_fingerprint, rank, offset)\u001b[39m\n\u001b[32m   3493\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m batched:\n\u001b[32m   3494\u001b[39m     _time = time.time()\n\u001b[32m-> \u001b[39m\u001b[32m3495\u001b[39m \u001b[43m    \u001b[49m\u001b[38;5;28;43;01mfor\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mi\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mexample\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;129;43;01min\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43miter_outputs\u001b[49m\u001b[43m(\u001b[49m\u001b[43mshard_iterable\u001b[49m\u001b[43m)\u001b[49m\u001b[43m:\u001b[49m\n\u001b[32m   3496\u001b[39m \u001b[43m        \u001b[49m\u001b[38;5;28;43;01mif\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mupdate_data\u001b[49m\u001b[43m:\u001b[49m\n\u001b[32m   3497\u001b[39m \u001b[43m            \u001b[49m\u001b[38;5;28;43;01mif\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mi\u001b[49m\u001b[43m \u001b[49m\u001b[43m==\u001b[49m\u001b[43m \u001b[49m\u001b[32;43m0\u001b[39;49m\u001b[43m:\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\arrow_dataset.py:3469\u001b[39m, in \u001b[36mDataset._map_single.<locals>.iter_outputs\u001b[39m\u001b[34m(shard_iterable)\u001b[39m\n\u001b[32m   3467\u001b[39m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m   3468\u001b[39m     \u001b[38;5;28;01mfor\u001b[39;00m i, example \u001b[38;5;129;01min\u001b[39;00m shard_iterable:\n\u001b[32m-> \u001b[39m\u001b[32m3469\u001b[39m         \u001b[38;5;28;01myield\u001b[39;00m i, \u001b[43mapply_function\u001b[49m\u001b[43m(\u001b[49m\u001b[43mexample\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mi\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43moffset\u001b[49m\u001b[43m=\u001b[49m\u001b[43moffset\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\arrow_dataset.py:3392\u001b[39m, in \u001b[36mDataset._map_single.<locals>.apply_function\u001b[39m\u001b[34m(pa_inputs, indices, offset)\u001b[39m\n\u001b[32m   3390\u001b[39m \u001b[38;5;250m\u001b[39m\u001b[33;03m\"\"\"Utility to apply the function on a selection of columns.\"\"\"\u001b[39;00m\n\u001b[32m   3391\u001b[39m inputs, fn_args, additional_args, fn_kwargs = prepare_inputs(pa_inputs, indices, offset=offset)\n\u001b[32m-> \u001b[39m\u001b[32m3392\u001b[39m processed_inputs = \u001b[43mfunction\u001b[49m\u001b[43m(\u001b[49m\u001b[43m*\u001b[49m\u001b[43mfn_args\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43madditional_args\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mfn_kwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   3393\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m prepare_outputs(pa_inputs, inputs, processed_inputs)\n",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[4]\u001b[39m\u001b[32m, line 2\u001b[39m, in \u001b[36mreplace_in_text\u001b[39m\u001b[34m(example)\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mreplace_in_text\u001b[39m(example):\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m     example[\u001b[33m\"\u001b[39m\u001b[33mcontext\u001b[39m\u001b[33m\"\u001b[39m] = \u001b[43mexample\u001b[49m\u001b[43m[\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mcontext\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m]\u001b[49m.replace(\u001b[33m\"\u001b[39m\u001b[33mjoyful\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33mhappy\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m      3\u001b[39m     example[\u001b[33m\"\u001b[39m\u001b[33mresponse\u001b[39m\u001b[33m\"\u001b[39m] = example[\u001b[33m\"\u001b[39m\u001b[33mresponse\u001b[39m\u001b[33m\"\u001b[39m].replace(\u001b[33m\"\u001b[39m\u001b[33mjoyful\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33mhappy\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m      4\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m example\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\formatting\\formatting.py:280\u001b[39m, in \u001b[36mLazyDict.__getitem__\u001b[39m\u001b[34m(self, key)\u001b[39m\n\u001b[32m    279\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34m__getitem__\u001b[39m(\u001b[38;5;28mself\u001b[39m, key):\n\u001b[32m--> \u001b[39m\u001b[32m280\u001b[39m     value = \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mdata\u001b[49m\u001b[43m[\u001b[49m\u001b[43mkey\u001b[49m\u001b[43m]\u001b[49m\n\u001b[32m    281\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m key \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mself\u001b[39m.keys_to_format:\n\u001b[32m    282\u001b[39m         value = \u001b[38;5;28mself\u001b[39m.format(key)\n",
      "\u001b[31mKeyError\u001b[39m: 'context'"
     ]
    }
   ],
   "source": [
    "def replace_in_text(example):\n",
    "    example[\"context\"] = example[\"context\"].replace(\"joyful\", \"happy\")\n",
    "    example[\"response\"] = example[\"response\"].replace(\"joyful\", \"happy\")\n",
    "    return example\n",
    "\n",
    "# Apply modification\n",
    "ds = ds.map(replace_in_text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9806849d-3c60-46f5-b3da-433cceffc84b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import AutoTokenizer, AutoModelForCausalLM\n",
    "\n",
    "# Load GPT-2 tokenizer\n",
    "tokenizer = AutoTokenizer.from_pretrained(\"gpt2\")\n",
    "tokenizer.pad_token = tokenizer.eos_token  # Set padding token\n",
    "\n",
    "# Load GPT-2 model\n",
    "model = AutoModelForCausalLM.from_pretrained(\"gpt2\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fdcd59f9-2717-42d5-b6fd-df8ae0222996",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "70d0429a7f0d48e189b796fb237604fa",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Map:   0%|          | 0/19209 [00:00<?, ? examples/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "bc66b6aedc674d83bc4aafe98ea1dcc0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Map:   0%|          | 0/2756 [00:00<?, ? examples/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "79d68a3f5f914070915553c35764f7f1",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Map:   0%|          | 0/2542 [00:00<?, ? examples/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "ename": "ValueError",
     "evalue": "Column name ['response'] not in the dataset. Current columns in the dataset: ['Unnamed: 0', 'situation', 'emotion', 'input_ids', 'attention_mask']",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mValueError\u001b[39m                                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[7]\u001b[39m\u001b[32m, line 8\u001b[39m\n\u001b[32m      5\u001b[39m tokenized_ds = ds.map(tokenize_function, batched=\u001b[38;5;28;01mTrue\u001b[39;00m)\n\u001b[32m      7\u001b[39m \u001b[38;5;66;03m# Remove original text columns to avoid errors\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m8\u001b[39m tokenized_ds = \u001b[43mtokenized_ds\u001b[49m\u001b[43m.\u001b[49m\u001b[43mremove_columns\u001b[49m\u001b[43m(\u001b[49m\u001b[43m[\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43msituation\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mresponse\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m)\u001b[49m  \u001b[38;5;66;03m# Keep only tokenized input\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\dataset_dict.py:364\u001b[39m, in \u001b[36mDatasetDict.remove_columns\u001b[39m\u001b[34m(self, column_names)\u001b[39m\n\u001b[32m    325\u001b[39m \u001b[38;5;250m\u001b[39m\u001b[33;03m\"\"\"\u001b[39;00m\n\u001b[32m    326\u001b[39m \u001b[33;03mRemove one or several column(s) from each split in the dataset\u001b[39;00m\n\u001b[32m    327\u001b[39m \u001b[33;03mand the features associated to the column(s).\u001b[39;00m\n\u001b[32m   (...)\u001b[39m\u001b[32m    361\u001b[39m \u001b[33;03m```\u001b[39;00m\n\u001b[32m    362\u001b[39m \u001b[33;03m\"\"\"\u001b[39;00m\n\u001b[32m    363\u001b[39m \u001b[38;5;28mself\u001b[39m._check_values_type()\n\u001b[32m--> \u001b[39m\u001b[32m364\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m DatasetDict({k: \u001b[43mdataset\u001b[49m\u001b[43m.\u001b[49m\u001b[43mremove_columns\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcolumn_names\u001b[49m\u001b[43m=\u001b[49m\u001b[43mcolumn_names\u001b[49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mfor\u001b[39;00m k, dataset \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mself\u001b[39m.items()})\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\arrow_dataset.py:562\u001b[39m, in \u001b[36mtransmit_format.<locals>.wrapper\u001b[39m\u001b[34m(*args, **kwargs)\u001b[39m\n\u001b[32m    555\u001b[39m self_format = {\n\u001b[32m    556\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mtype\u001b[39m\u001b[33m\"\u001b[39m: \u001b[38;5;28mself\u001b[39m._format_type,\n\u001b[32m    557\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mformat_kwargs\u001b[39m\u001b[33m\"\u001b[39m: \u001b[38;5;28mself\u001b[39m._format_kwargs,\n\u001b[32m    558\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mcolumns\u001b[39m\u001b[33m\"\u001b[39m: \u001b[38;5;28mself\u001b[39m._format_columns,\n\u001b[32m    559\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33moutput_all_columns\u001b[39m\u001b[33m\"\u001b[39m: \u001b[38;5;28mself\u001b[39m._output_all_columns,\n\u001b[32m    560\u001b[39m }\n\u001b[32m    561\u001b[39m \u001b[38;5;66;03m# apply actual function\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m562\u001b[39m out: Union[\u001b[33m\"\u001b[39m\u001b[33mDataset\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33mDatasetDict\u001b[39m\u001b[33m\"\u001b[39m] = \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    563\u001b[39m datasets: List[\u001b[33m\"\u001b[39m\u001b[33mDataset\u001b[39m\u001b[33m\"\u001b[39m] = \u001b[38;5;28mlist\u001b[39m(out.values()) \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(out, \u001b[38;5;28mdict\u001b[39m) \u001b[38;5;28;01melse\u001b[39;00m [out]\n\u001b[32m    564\u001b[39m \u001b[38;5;66;03m# re-apply format to the output\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\fingerprint.py:442\u001b[39m, in \u001b[36mfingerprint_transform.<locals>._fingerprint.<locals>.wrapper\u001b[39m\u001b[34m(*args, **kwargs)\u001b[39m\n\u001b[32m    438\u001b[39m             validate_fingerprint(kwargs[fingerprint_name])\n\u001b[32m    440\u001b[39m \u001b[38;5;66;03m# Call actual function\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m442\u001b[39m out = \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[43mdataset\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    444\u001b[39m \u001b[38;5;66;03m# Update fingerprint of in-place transforms + update in-place history of transforms\u001b[39;00m\n\u001b[32m    446\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m inplace:  \u001b[38;5;66;03m# update after calling func so that the fingerprint doesn't change if the function fails\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\arrow_dataset.py:2166\u001b[39m, in \u001b[36mDataset.remove_columns\u001b[39m\u001b[34m(self, column_names, new_fingerprint)\u001b[39m\n\u001b[32m   2164\u001b[39m missing_columns = \u001b[38;5;28mset\u001b[39m(column_names) - \u001b[38;5;28mset\u001b[39m(\u001b[38;5;28mself\u001b[39m._data.column_names)\n\u001b[32m   2165\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m missing_columns:\n\u001b[32m-> \u001b[39m\u001b[32m2166\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[32m   2167\u001b[39m         \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mColumn name \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mlist\u001b[39m(missing_columns)\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m not in the dataset. \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m   2168\u001b[39m         \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mCurrent columns in the dataset: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mdataset._data.column_names\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m\"\u001b[39m\n\u001b[32m   2169\u001b[39m     )\n\u001b[32m   2171\u001b[39m \u001b[38;5;28;01mfor\u001b[39;00m column_name \u001b[38;5;129;01min\u001b[39;00m column_names:\n\u001b[32m   2172\u001b[39m     \u001b[38;5;28;01mdel\u001b[39;00m dataset._info.features[column_name]\n",
      "\u001b[31mValueError\u001b[39m: Column name ['response'] not in the dataset. Current columns in the dataset: ['Unnamed: 0', 'situation', 'emotion', 'input_ids', 'attention_mask']"
     ]
    }
   ],
   "source": [
    "def tokenize_function(examples):\n",
    "    return tokenizer(examples[\"situation\"], truncation=True, padding=\"max_length\", max_length=128)\n",
    "\n",
    "# Apply tokenization\n",
    "tokenized_ds = ds.map(tokenize_function, batched=True)\n",
    "\n",
    "# Remove original text columns to avoid errors\n",
    "tokenized_ds = tokenized_ds.remove_columns([\"situation\", \"response\"])  # Keep only tokenized input\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "52cffc24-2fc6-4465-94b1-b183f11bfe02",
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import GPT2LMHeadModel, GPT2Tokenizer\n",
    "\n",
    "# Load pre-trained GPT-2 model and tokenizer\n",
    "model_name = \"gpt2\"\n",
    "tokenizer = GPT2Tokenizer.from_pretrained(model_name)\n",
    "model = GPT2LMHeadModel.from_pretrained(model_name)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "542ba842-b725-4adf-866c-ea7f20e9b089",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "The attention mask and the pad token id were not set. As a consequence, you may observe unexpected behavior. Please pass your input's `attention_mask` to obtain reliable results.\n",
      "Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.\n",
      "The attention mask is not set and cannot be inferred from input because pad token is same as eos token. As a consequence, you may observe unexpected behavior. Please pass your input's `attention_mask` to obtain reliable results.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I'm not sure what to say. I'm not sure what to say. I'm not sure what\n"
     ]
    }
   ],
   "source": [
    "import torch\n",
    "\n",
    "def generate_response(situation, emotion, max_length=50):\n",
    "    prompt = f\"Situation: {situation} Emotion: {emotion} Response:\"\n",
    "    input_ids = tokenizer.encode(prompt, return_tensors=\"pt\")\n",
    "\n",
    "    # Generate output\n",
    "    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)\n",
    "    \n",
    "    # Decode the generated text\n",
    "    response = tokenizer.decode(output[0], skip_special_tokens=True)\n",
    "    return response.split(\"Response:\")[-1].strip()  # Extract only the response part\n",
    "\n",
    "# Example usage\n",
    "situation = \"I remember going to the fireworks with my best friend. It felt like just us in the world.\"\n",
    "emotion = \"sentimental\"\n",
    "\n",
    "generated_response = generate_response(situation, emotion)\n",
    "print(generated_response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f6735169-549a-4765-9e64-abc7a9e82576",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Well, you see, it's a big world. There are so many people. Everyone gets together and\n"
     ]
    }
   ],
   "source": [
    "import torch\n",
    "from transformers import GPT2LMHeadModel, GPT2Tokenizer\n",
    "\n",
    "# Load GPT-2 and tokenizer\n",
    "model_name = \"gpt2\"\n",
    "tokenizer = GPT2Tokenizer.from_pretrained(model_name)\n",
    "model = GPT2LMHeadModel.from_pretrained(model_name)\n",
    "\n",
    "# Fix padding issue\n",
    "tokenizer.pad_token = tokenizer.eos_token\n",
    "model.config.pad_token_id = tokenizer.eos_token_id\n",
    "\n",
    "def generate_response(situation, emotion, max_length=50):\n",
    "    prompt = f\"Situation: {situation} Emotion: {emotion} Response:\"\n",
    "    input_ids = tokenizer.encode(prompt, return_tensors=\"pt\")\n",
    "    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)  # Attention mask\n",
    "\n",
    "    # Generate output with better sampling\n",
    "    output = model.generate(\n",
    "        input_ids, \n",
    "        attention_mask=attention_mask,\n",
    "        max_length=max_length,  \n",
    "        num_return_sequences=1,\n",
    "        do_sample=True,  # Enable sampling\n",
    "        top_k=50,  # Limit to top 50 words\n",
    "        top_p=0.95,  # Nucleus sampling\n",
    "        temperature=0.7,  # Reduce repetition\n",
    "    )\n",
    "\n",
    "    response = tokenizer.decode(output[0], skip_special_tokens=True)\n",
    "    return response.split(\"Response:\")[-1].strip()  # Extract response\n",
    "\n",
    "# Test it again\n",
    "situation = \"I remember going to the fireworks with my best friend. It felt like just us in the world.\"\n",
    "emotion = \"sentimental\"\n",
    "\n",
    "generated_response = generate_response(situation, emotion)\n",
    "print(generated_response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "34437f69-d182-4d0c-b62d-517c3df3ffb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I'm glad that there was so much love and support for me because it's a\n"
     ]
    }
   ],
   "source": [
    "import torch\n",
    "from transformers import GPT2LMHeadModel, GPT2Tokenizer\n",
    "\n",
    "# Load GPT-2 model and tokenizer\n",
    "model_name = \"gpt2\"\n",
    "tokenizer = GPT2Tokenizer.from_pretrained(model_name)\n",
    "model = GPT2LMHeadModel.from_pretrained(model_name)\n",
    "\n",
    "# Set padding token\n",
    "tokenizer.pad_token = tokenizer.eos_token\n",
    "model.config.pad_token_id = tokenizer.eos_token_id\n",
    "\n",
    "def generate_response(situation, emotion, max_length=50):\n",
    "    # Improve prompt with an example format\n",
    "    prompt = (\n",
    "        f\"Situation: {situation}\\n\"\n",
    "        f\"Emotion: {emotion}\\n\"\n",
    "        f\"Response: \"\n",
    "    )\n",
    "    \n",
    "    input_ids = tokenizer.encode(prompt, return_tensors=\"pt\")\n",
    "    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)  # Use attention mask\n",
    "\n",
    "    # Generate response with improved decoding\n",
    "    output = model.generate(\n",
    "        input_ids, \n",
    "        attention_mask=attention_mask,\n",
    "        max_length=max_length,\n",
    "        num_return_sequences=1,\n",
    "        do_sample=True,\n",
    "        top_k=50,\n",
    "        top_p=0.9,\n",
    "        temperature=0.8,\n",
    "        repetition_penalty=1.2,  # Reduce looping responses\n",
    "        eos_token_id=tokenizer.eos_token_id,  # Ensure stopping\n",
    "    )\n",
    "\n",
    "    response = tokenizer.decode(output[0], skip_special_tokens=True)\n",
    "\n",
    "    # Extract generated response text after \"Response:\"\n",
    "    return response.split(\"Response:\")[-1].strip()\n",
    "\n",
    "# Test with a situation\n",
    "situation = \"I remember going to the fireworks with my best friend. It felt like just us in the world.\"\n",
    "emotion = \"sentimental\"\n",
    "\n",
    "generated_response = generate_response(situation, emotion)\n",
    "print(generated_response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "3bef0e19-67f9-489e-b890-5e8d2a4c9f16",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "?????? i dont know much about this but here is what I would like to share with ya. my father started working in the construction industry as a teacher and he was very important part of his school's life -.\n"
     ]
    }
   ],
   "source": [
    "import torch\n",
    "from transformers import GPT2LMHeadModel, GPT2Tokenizer\n",
    "\n",
    "# Load GPT-2 model and tokenizer\n",
    "model_name = \"gpt2\"\n",
    "tokenizer = GPT2Tokenizer.from_pretrained(model_name)\n",
    "model = GPT2LMHeadModel.from_pretrained(model_name)\n",
    "\n",
    "# Set padding token\n",
    "tokenizer.pad_token = tokenizer.eos_token\n",
    "model.config.pad_token_id = tokenizer.eos_token_id\n",
    "\n",
    "def generate_response(situation, emotion, max_length=60):\n",
    "    # Improve prompt clarity\n",
    "    prompt = (\n",
    "        f\"Situation: {situation}\\n\"\n",
    "        f\"Emotion: {emotion}\\n\"\n",
    "        f\"Response: \"\n",
    "    )\n",
    "    \n",
    "    input_ids = tokenizer.encode(prompt, return_tensors=\"pt\")\n",
    "    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)  \n",
    "\n",
    "    # Generate response with controlled randomness\n",
    "    output = model.generate(\n",
    "        input_ids, \n",
    "        attention_mask=attention_mask,\n",
    "        max_length=max_length,  # Ensure full response generation\n",
    "        num_return_sequences=1,\n",
    "        do_sample=True,\n",
    "        top_k=50,  # Keep words diverse\n",
    "        top_p=0.95,  # Avoid nonsense\n",
    "        temperature=0.7,  # Make it sound natural\n",
    "        repetition_penalty=1.3,  # Reduce looping phrases\n",
    "        eos_token_id=tokenizer.eos_token_id,  # Ensure stopping\n",
    "    )\n",
    "\n",
    "    response = tokenizer.decode(output[0], skip_special_tokens=True)\n",
    "\n",
    "    # Extract generated response text after \"Response:\"\n",
    "    response_text = response.split(\"Response:\")[-1].strip()\n",
    "\n",
    "    # Apply a simple stop condition to avoid unfinished sentences\n",
    "    if not response_text.endswith((\".\", \"!\", \"?\")):\n",
    "        response_text += \".\"\n",
    "\n",
    "    return response_text\n",
    "\n",
    "# Test with a sample situation\n",
    "situation = \"hi how are you?\"\n",
    "emotion = \"\"\n",
    "\n",
    "generated_response = generate_response(situation, emotion)\n",
    "print(generated_response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "48219a5a-0035-4cb0-8b79-22f53e2e1590",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Manually creating sample responses\n",
    "response_data = {\n",
    "    \"situation\": [\n",
    "        \"I remember going to the fireworks with my best friend.\",\n",
    "        \"I failed my exam despite studying a lot.\",\n",
    "        \"I got a promotion at work today!\",\n",
    "        \"I lost my job unexpectedly.\"\n",
    "    ],\n",
    "    \"emotion\": [\"sentimental\", \"sad\", \"happy\", \"sad\"],\n",
    "    \"response\": [\n",
    "        \"That sounds like a magical moment! Fireworks make everything feel special.\",\n",
    "        \"I'm sorry to hear that. It must be frustrating after all your hard work.\",\n",
    "        \"Congratulations! You truly deserved this achievement.\",\n",
    "        \"That must be really tough. Do you have any backup plans?\"\n",
    "    ]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(response_data)\n",
    "df.to_csv(\"emotion_responses.csv\", index=False)  # Save dataset for training\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4680fe9e-d707-4fd7-9275-20aee3b27ad9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "dab3b0dc43b04c688ad6894067548a43",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Generating train split: 0 examples [00:00, ? examples/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8ba472f9bf854c3fbf285c75c8788b76",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Map:   0%|          | 0/4 [00:00<?, ? examples/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "ename": "ArrowInvalid",
     "evalue": "Column 3 named input_ids expected length 4 but got length 100",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mArrowInvalid\u001b[39m                              Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[16]\u001b[39m\u001b[32m, line 17\u001b[39m\n\u001b[32m     14\u001b[39m     text = \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mSituation: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mexample[\u001b[33m'\u001b[39m\u001b[33msituation\u001b[39m\u001b[33m'\u001b[39m]\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m Emotion: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mexample[\u001b[33m'\u001b[39m\u001b[33memotion\u001b[39m\u001b[33m'\u001b[39m]\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m Response: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mexample[\u001b[33m'\u001b[39m\u001b[33mresponse\u001b[39m\u001b[33m'\u001b[39m]\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m\"\u001b[39m\n\u001b[32m     15\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m tokenizer(text, truncation=\u001b[38;5;28;01mTrue\u001b[39;00m, padding=\u001b[33m\"\u001b[39m\u001b[33mmax_length\u001b[39m\u001b[33m\"\u001b[39m, max_length=\u001b[32m100\u001b[39m)\n\u001b[32m---> \u001b[39m\u001b[32m17\u001b[39m tokenized_ds = \u001b[43mdataset\u001b[49m\u001b[43m.\u001b[49m\u001b[43mmap\u001b[49m\u001b[43m(\u001b[49m\u001b[43mtokenize_function\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mbatched\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43;01mTrue\u001b[39;49;00m\u001b[43m)\u001b[49m\n\u001b[32m     19\u001b[39m \u001b[38;5;66;03m# Training arguments\u001b[39;00m\n\u001b[32m     20\u001b[39m training_args = TrainingArguments(\n\u001b[32m     21\u001b[39m     output_dir=\u001b[33m\"\u001b[39m\u001b[33m./gpt2_emotion\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m     22\u001b[39m     evaluation_strategy=\u001b[33m\"\u001b[39m\u001b[33mepoch\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m   (...)\u001b[39m\u001b[32m     28\u001b[39m     logging_dir=\u001b[33m\"\u001b[39m\u001b[33m./logs\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m     29\u001b[39m )\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\dataset_dict.py:902\u001b[39m, in \u001b[36mDatasetDict.map\u001b[39m\u001b[34m(self, function, with_indices, with_rank, input_columns, batched, batch_size, drop_last_batch, remove_columns, keep_in_memory, load_from_cache_file, cache_file_names, writer_batch_size, features, disable_nullable, fn_kwargs, num_proc, desc)\u001b[39m\n\u001b[32m    898\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m cache_file_names \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[32m    899\u001b[39m     cache_file_names = {k: \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;28;01mfor\u001b[39;00m k \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mself\u001b[39m}\n\u001b[32m    900\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m DatasetDict(\n\u001b[32m    901\u001b[39m     {\n\u001b[32m--> \u001b[39m\u001b[32m902\u001b[39m         k: \u001b[43mdataset\u001b[49m\u001b[43m.\u001b[49m\u001b[43mmap\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m    903\u001b[39m \u001b[43m            \u001b[49m\u001b[43mfunction\u001b[49m\u001b[43m=\u001b[49m\u001b[43mfunction\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    904\u001b[39m \u001b[43m            \u001b[49m\u001b[43mwith_indices\u001b[49m\u001b[43m=\u001b[49m\u001b[43mwith_indices\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    905\u001b[39m \u001b[43m            \u001b[49m\u001b[43mwith_rank\u001b[49m\u001b[43m=\u001b[49m\u001b[43mwith_rank\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    906\u001b[39m \u001b[43m            \u001b[49m\u001b[43minput_columns\u001b[49m\u001b[43m=\u001b[49m\u001b[43minput_columns\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    907\u001b[39m \u001b[43m            \u001b[49m\u001b[43mbatched\u001b[49m\u001b[43m=\u001b[49m\u001b[43mbatched\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    908\u001b[39m \u001b[43m            \u001b[49m\u001b[43mbatch_size\u001b[49m\u001b[43m=\u001b[49m\u001b[43mbatch_size\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    909\u001b[39m \u001b[43m            \u001b[49m\u001b[43mdrop_last_batch\u001b[49m\u001b[43m=\u001b[49m\u001b[43mdrop_last_batch\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    910\u001b[39m \u001b[43m            \u001b[49m\u001b[43mremove_columns\u001b[49m\u001b[43m=\u001b[49m\u001b[43mremove_columns\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    911\u001b[39m \u001b[43m            \u001b[49m\u001b[43mkeep_in_memory\u001b[49m\u001b[43m=\u001b[49m\u001b[43mkeep_in_memory\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    912\u001b[39m \u001b[43m            \u001b[49m\u001b[43mload_from_cache_file\u001b[49m\u001b[43m=\u001b[49m\u001b[43mload_from_cache_file\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    913\u001b[39m \u001b[43m            \u001b[49m\u001b[43mcache_file_name\u001b[49m\u001b[43m=\u001b[49m\u001b[43mcache_file_names\u001b[49m\u001b[43m[\u001b[49m\u001b[43mk\u001b[49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    914\u001b[39m \u001b[43m            \u001b[49m\u001b[43mwriter_batch_size\u001b[49m\u001b[43m=\u001b[49m\u001b[43mwriter_batch_size\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    915\u001b[39m \u001b[43m            \u001b[49m\u001b[43mfeatures\u001b[49m\u001b[43m=\u001b[49m\u001b[43mfeatures\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    916\u001b[39m \u001b[43m            \u001b[49m\u001b[43mdisable_nullable\u001b[49m\u001b[43m=\u001b[49m\u001b[43mdisable_nullable\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    917\u001b[39m \u001b[43m            \u001b[49m\u001b[43mfn_kwargs\u001b[49m\u001b[43m=\u001b[49m\u001b[43mfn_kwargs\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    918\u001b[39m \u001b[43m            \u001b[49m\u001b[43mnum_proc\u001b[49m\u001b[43m=\u001b[49m\u001b[43mnum_proc\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    919\u001b[39m \u001b[43m            \u001b[49m\u001b[43mdesc\u001b[49m\u001b[43m=\u001b[49m\u001b[43mdesc\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    920\u001b[39m \u001b[43m        \u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    921\u001b[39m         \u001b[38;5;28;01mfor\u001b[39;00m k, dataset \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mself\u001b[39m.items()\n\u001b[32m    922\u001b[39m     }\n\u001b[32m    923\u001b[39m )\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\arrow_dataset.py:562\u001b[39m, in \u001b[36mtransmit_format.<locals>.wrapper\u001b[39m\u001b[34m(*args, **kwargs)\u001b[39m\n\u001b[32m    555\u001b[39m self_format = {\n\u001b[32m    556\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mtype\u001b[39m\u001b[33m\"\u001b[39m: \u001b[38;5;28mself\u001b[39m._format_type,\n\u001b[32m    557\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mformat_kwargs\u001b[39m\u001b[33m\"\u001b[39m: \u001b[38;5;28mself\u001b[39m._format_kwargs,\n\u001b[32m    558\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mcolumns\u001b[39m\u001b[33m\"\u001b[39m: \u001b[38;5;28mself\u001b[39m._format_columns,\n\u001b[32m    559\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33moutput_all_columns\u001b[39m\u001b[33m\"\u001b[39m: \u001b[38;5;28mself\u001b[39m._output_all_columns,\n\u001b[32m    560\u001b[39m }\n\u001b[32m    561\u001b[39m \u001b[38;5;66;03m# apply actual function\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m562\u001b[39m out: Union[\u001b[33m\"\u001b[39m\u001b[33mDataset\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33mDatasetDict\u001b[39m\u001b[33m\"\u001b[39m] = \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    563\u001b[39m datasets: List[\u001b[33m\"\u001b[39m\u001b[33mDataset\u001b[39m\u001b[33m\"\u001b[39m] = \u001b[38;5;28mlist\u001b[39m(out.values()) \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(out, \u001b[38;5;28mdict\u001b[39m) \u001b[38;5;28;01melse\u001b[39;00m [out]\n\u001b[32m    564\u001b[39m \u001b[38;5;66;03m# re-apply format to the output\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\arrow_dataset.py:3079\u001b[39m, in \u001b[36mDataset.map\u001b[39m\u001b[34m(self, function, with_indices, with_rank, input_columns, batched, batch_size, drop_last_batch, remove_columns, keep_in_memory, load_from_cache_file, cache_file_name, writer_batch_size, features, disable_nullable, fn_kwargs, num_proc, suffix_template, new_fingerprint, desc)\u001b[39m\n\u001b[32m   3073\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m transformed_dataset \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[32m   3074\u001b[39m     \u001b[38;5;28;01mwith\u001b[39;00m hf_tqdm(\n\u001b[32m   3075\u001b[39m         unit=\u001b[33m\"\u001b[39m\u001b[33m examples\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m   3076\u001b[39m         total=pbar_total,\n\u001b[32m   3077\u001b[39m         desc=desc \u001b[38;5;129;01mor\u001b[39;00m \u001b[33m\"\u001b[39m\u001b[33mMap\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m   3078\u001b[39m     ) \u001b[38;5;28;01mas\u001b[39;00m pbar:\n\u001b[32m-> \u001b[39m\u001b[32m3079\u001b[39m \u001b[43m        \u001b[49m\u001b[38;5;28;43;01mfor\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mrank\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mdone\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcontent\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;129;43;01min\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mDataset\u001b[49m\u001b[43m.\u001b[49m\u001b[43m_map_single\u001b[49m\u001b[43m(\u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mdataset_kwargs\u001b[49m\u001b[43m)\u001b[49m\u001b[43m:\u001b[49m\n\u001b[32m   3080\u001b[39m \u001b[43m            \u001b[49m\u001b[38;5;28;43;01mif\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43mdone\u001b[49m\u001b[43m:\u001b[49m\n\u001b[32m   3081\u001b[39m \u001b[43m                \u001b[49m\u001b[43mshards_done\u001b[49m\u001b[43m \u001b[49m\u001b[43m+\u001b[49m\u001b[43m=\u001b[49m\u001b[43m \u001b[49m\u001b[32;43m1\u001b[39;49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\arrow_dataset.py:3534\u001b[39m, in \u001b[36mDataset._map_single\u001b[39m\u001b[34m(shard, function, with_indices, with_rank, input_columns, batched, batch_size, drop_last_batch, remove_columns, keep_in_memory, cache_file_name, writer_batch_size, features, disable_nullable, fn_kwargs, new_fingerprint, rank, offset)\u001b[39m\n\u001b[32m   3532\u001b[39m         writer.write_table(batch.to_arrow())\n\u001b[32m   3533\u001b[39m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m-> \u001b[39m\u001b[32m3534\u001b[39m         \u001b[43mwriter\u001b[49m\u001b[43m.\u001b[49m\u001b[43mwrite_batch\u001b[49m\u001b[43m(\u001b[49m\u001b[43mbatch\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   3535\u001b[39m num_examples_progress_update += num_examples_in_batch\n\u001b[32m   3536\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m time.time() > _time + config.PBAR_REFRESH_TIME_INTERVAL:\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\datasets\\arrow_writer.py:608\u001b[39m, in \u001b[36mArrowWriter.write_batch\u001b[39m\u001b[34m(self, batch_examples, writer_batch_size)\u001b[39m\n\u001b[32m    606\u001b[39m         inferred_features[col] = typed_sequence.get_inferred_type()\n\u001b[32m    607\u001b[39m schema = inferred_features.arrow_schema \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m.pa_writer \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;28;01melse\u001b[39;00m \u001b[38;5;28mself\u001b[39m.schema\n\u001b[32m--> \u001b[39m\u001b[32m608\u001b[39m pa_table = \u001b[43mpa\u001b[49m\u001b[43m.\u001b[49m\u001b[43mTable\u001b[49m\u001b[43m.\u001b[49m\u001b[43mfrom_arrays\u001b[49m\u001b[43m(\u001b[49m\u001b[43marrays\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mschema\u001b[49m\u001b[43m=\u001b[49m\u001b[43mschema\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    609\u001b[39m \u001b[38;5;28mself\u001b[39m.write_table(pa_table, writer_batch_size)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\pyarrow\\table.pxi:4868\u001b[39m, in \u001b[36mpyarrow.lib.Table.from_arrays\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\pyarrow\\table.pxi:4214\u001b[39m, in \u001b[36mpyarrow.lib.Table.validate\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Roaming\\Python\\Python313\\site-packages\\pyarrow\\error.pxi:92\u001b[39m, in \u001b[36mpyarrow.lib.check_status\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[31mArrowInvalid\u001b[39m: Column 3 named input_ids expected length 4 but got length 100"
     ]
    }
   ],
   "source": [
    "from datasets import load_dataset\n",
    "from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling\n",
    "\n",
    "# Load dataset (after creating it)\n",
    "dataset = load_dataset(\"csv\", data_files=\"emotion_responses.csv\")\n",
    "\n",
    "# Load tokenizer and model\n",
    "tokenizer = GPT2Tokenizer.from_pretrained(\"gpt2\")\n",
    "tokenizer.pad_token = tokenizer.eos_token  # Set pad token\n",
    "model = GPT2LMHeadModel.from_pretrained(\"gpt2\")\n",
    "\n",
    "# Tokenize the dataset\n",
    "def tokenize_function(example):\n",
    "    text = f\"Situation: {example['situation']} Emotion: {example['emotion']} Response: {example['response']}\"\n",
    "    return tokenizer(text, truncation=True, padding=\"max_length\", max_length=100)\n",
    "\n",
    "tokenized_ds = dataset.map(tokenize_function, batched=True)\n",
    "\n",
    "# Training arguments\n",
    "training_args = TrainingArguments(\n",
    "    output_dir=\"./gpt2_emotion\",\n",
    "    evaluation_strategy=\"epoch\",\n",
    "    per_device_train_batch_size=8,\n",
    "    per_device_eval_batch_size=8,\n",
    "    num_train_epochs=3,\n",
    "    save_steps=500,\n",
    "    save_total_limit=2,\n",
    "    logging_dir=\"./logs\",\n",
    ")\n",
    "\n",
    "trainer = Trainer(\n",
    "    model=model,\n",
    "    args=training_args,\n",
    "    train_dataset=tokenized_ds[\"train\"],\n",
    "    eval_dataset=tokenized_ds[\"validation\"],\n",
    "    tokenizer=tokenizer,\n",
    "    data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False),\n",
    ")\n",
    "\n",
    "# Train the model\n",
    "trainer.train()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "9aacf7ad-5b1c-4d54-800d-0704762661fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "bdcd2a4818374497b86db44abc1ecc83",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Map:   0%|          | 0/4 [00:00<?, ? examples/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'input_ids': 46655, 'attention_mask': 1}\n"
     ]
    }
   ],
   "source": [
    "from transformers import GPT2Tokenizer\n",
    "\n",
    "# Load GPT-2 tokenizer\n",
    "tokenizer = GPT2Tokenizer.from_pretrained(\"gpt2\")\n",
    "tokenizer.pad_token = tokenizer.eos_token  # Set pad token\n",
    "\n",
    "# Define tokenization function\n",
    "def tokenize_function(example):\n",
    "    text = f\"Situation: {example['situation']} Emotion: {example['emotion']} Response: {example['response']}\"\n",
    "    \n",
    "    # Tokenize properly\n",
    "    encoding = tokenizer(text, truncation=True, padding=\"max_length\", max_length=100)\n",
    "    \n",
    "    return { \n",
    "        \"input_ids\": encoding[\"input_ids\"], \n",
    "        \"attention_mask\": encoding[\"attention_mask\"] \n",
    "    }\n",
    "\n",
    "# Apply tokenization correctly\n",
    "tokenized_ds = dataset.map(tokenize_function, batched=True, remove_columns=dataset[\"train\"].column_names)\n",
    "\n",
    "# Check the structure\n",
    "print(tokenized_ds[\"train\"][0])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "62dc4def-1f39-4441-bc91-f5337a95158b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'situation': 'I remember going to the fireworks with my best friend.', 'emotion': 'sentimental', 'response': 'That sounds like a magical moment! Fireworks make everything feel special.'}\n"
     ]
    }
   ],
   "source": [
    "from datasets import load_dataset\n",
    "\n",
    "# Load dataset\n",
    "dataset = load_dataset(\"csv\", data_files=\"emotion_responses.csv\")\n",
    "\n",
    "# Print sample row to verify structure\n",
    "print(dataset[\"train\"][0])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "71a8e455-0924-42ca-98d7-b16f5f07733c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'input_ids': 46655, 'attention_mask': 1}\n"
     ]
    }
   ],
   "source": [
    "from transformers import GPT2Tokenizer\n",
    "\n",
    "# Load GPT-2 tokenizer\n",
    "tokenizer = GPT2Tokenizer.from_pretrained(\"gpt2\")\n",
    "tokenizer.pad_token = tokenizer.eos_token  # Set pad token\n",
    "\n",
    "# Define tokenization function\n",
    "def tokenize_function(example):\n",
    "    text = f\"Situation: {example['situation']} Emotion: {example['emotion']} Response: {example['response']}\"\n",
    "    \n",
    "    # Tokenize properly\n",
    "    encoding = tokenizer(text, truncation=True, padding=\"max_length\", max_length=100)\n",
    "    \n",
    "    return { \n",
    "        \"input_ids\": encoding[\"input_ids\"], \n",
    "        \"attention_mask\": encoding[\"attention_mask\"] \n",
    "    }\n",
    "\n",
    "# Apply tokenization correctly\n",
    "tokenized_ds = dataset.map(tokenize_function, batched=True, remove_columns=dataset[\"train\"].column_names)\n",
    "\n",
    "# Check the structure\n",
    "print(tokenized_ds[\"train\"][0])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "827acf26-4b63-4dc9-a7d4-8cb922b0db8d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "The attention mask and the pad token id were not set. As a consequence, you may observe unexpected behavior. Please pass your input's `attention_mask` to obtain reliable results.\n",
      "Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\"What did you think? What kind of person do you want to be?\" [In an angry tone, the Student Council president] \"It's not about me.\" You have done this before by being so outspoken in your own words and actions that it feels like someone has been punished for expressing their feelings on campus or anywhere else they can feel guilty with something as obvious at hand (like yelling obscen\n"
     ]
    }
   ],
   "source": [
    "def generate_response(situation, emotion):\n",
    "    prompt = f\"Situation: {situation} Emotion: {emotion} Response:\"\n",
    "    input_ids = tokenizer.encode(prompt, return_tensors=\"pt\")\n",
    "\n",
    "    output = model.generate(\n",
    "        input_ids,\n",
    "        max_length=100,\n",
    "        num_return_sequences=1,\n",
    "        do_sample=True,\n",
    "        top_k=50,\n",
    "        top_p=0.9,\n",
    "        temperature=0.7,\n",
    "        repetition_penalty=1.3,\n",
    "        eos_token_id=tokenizer.eos_token_id,\n",
    "    )\n",
    "\n",
    "    response = tokenizer.decode(output[0], skip_special_tokens=True)\n",
    "    return response.split(\"Response:\")[-1].strip()  # Extract only the response\n",
    "\n",
    "# Test it after training\n",
    "situation = \"I failed my exam despite studying a lot.\"\n",
    "emotion = \"sad\"\n",
    "print(generate_response(situation, emotion))  # Should generate a more relevant response\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "fd564b35-de96-4f66-8cae-34bd908dd4ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "def format_input(example):\n",
    "    return f\"Situation: {example['situation']} Emotion: {example['emotion']} Response:\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "224e20d4-47cf-48e5-a01e-a12059dff1dd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3f7663752fbc421d84cf02b6d738681e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Map:   0%|          | 0/4 [00:00<?, ? examples/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from transformers import GPT2Tokenizer\n",
    "\n",
    "# Load GPT-2 tokenizer\n",
    "tokenizer = GPT2Tokenizer.from_pretrained(\"gpt2\")\n",
    "tokenizer.pad_token = tokenizer.eos_token  # Set padding token\n",
    "\n",
    "# Tokenization function\n",
    "def tokenize_function(example):\n",
    "    text = format_input(example)\n",
    "    \n",
    "    encoding = tokenizer(\n",
    "        text,\n",
    "        truncation=True,\n",
    "        padding=\"max_length\",\n",
    "        max_length=100\n",
    "    )\n",
    "\n",
    "    return { \n",
    "        \"input_ids\": encoding[\"input_ids\"], \n",
    "        \"attention_mask\": encoding[\"attention_mask\"] \n",
    "    }\n",
    "\n",
    "# Apply tokenization\n",
    "tokenized_ds = dataset.map(tokenize_function, batched=True, remove_columns=dataset[\"train\"].column_names)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "812463af-9a75-4b23-a413-516eca620bdc",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Device set to use cpu\n",
      "Truncation was not explicitly activated but `max_length` is provided a specific value, please use `truncation=True` to explicitly truncate examples to max length. Defaulting to 'longest_first' truncation strategy. If you encode pairs of sequences (GLUE-style) with the tokenizer you can select this strategy more precisely by providing a specific strategy to `truncation`.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Situation: I failed my exam despite studying a lot. Emotion: frustrated Response: How do you feel this year in terms of emotions? The person with the red hair: I don't think the emotions were so different. Emotion: frustrated\n"
     ]
    }
   ],
   "source": [
    "from transformers import GPT2LMHeadModel, pipeline\n",
    "\n",
    "# Load fine-tuned GPT-2 model\n",
    "model = GPT2LMHeadModel.from_pretrained(\"gpt2\")\n",
    "\n",
    "# Create pipeline for generation\n",
    "generator = pipeline(\"text-generation\", model=model, tokenizer=tokenizer)\n",
    "\n",
    "# Example input\n",
    "situation = \"I failed my exam despite studying a lot.\"\n",
    "emotion = \"frustrated\"\n",
    "\n",
    "input_text = f\"Situation: {situation} Emotion: {emotion} Response:\"\n",
    "output = generator(input_text, max_length=50, num_return_sequences=1)\n",
    "\n",
    "print(output[0][\"generated_text\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da262e2e-b97d-49d3-80a0-45991e89de39",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
