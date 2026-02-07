
# Capitolo 11 – Ray & Modin (codice di supporto)

Questo pacchetto raccoglie notebook e script per gli esempi del capitolo 11:
- **Ray**: task, actor, Monte Carlo π, Train/Tune/Serve
- **Modin**: alternative parallela a Pandas e micro‑benchmark

## Requisiti principali
Consigliato Python 3.10+ in ambiente virtuale/conda.

### Installazione rapida (CPU)
```bash
pip install -U ray "ray[tune,train,serve]" modin[ray] pandas numpy torch torchvision pillow requests
```

> **Nota**: per Ray Serve sono usati componenti Starlette/FastAPI inclusi nelle extra di `ray[serve]`.
> Per GPU con PyTorch, seguire le istruzioni ufficiali su https://pytorch.org get-started.

## Contenuto
- `notebooks/`
  - `11a_ray_basics_tasks_actors.ipynb`
  - `11b_ray_monte_carlo_pi.ipynb`
  - `11c_ray_tune_train_fashionmnist.ipynb`
  - `11d_train_final_model.ipynb`
  - `11e_ray_serve_deploy.ipynb`
  - `11f_modin_intro_benchmarks.ipynb`
- `scripts/`
  - `11g_tune_model.py`
  - `11h_final_model.py`
  - `11i_serve_model.py`
  - `11j_generate_mnist_image.py`
  - `11k_ray_monte_carlo.py`
- `data/`
  - `employees.csv` (piccolo esempio)
  - `fashion_metadata.csv` (esempio per preprocess Modin)

## Note d’uso rapide
- I notebook impostano configurazioni "light" (pochissime epoche/campionamenti) per girare anche su macchine modeste.
- Gli script CLI riprendono le versioni "piene" (modifica parametri via codice/argomenti).
- Per **Serve**, prima salva/allenare `fashion_cnn.pth` con `11h_final_model.py` o notebook equivalente, poi:
  ```bash
  serve run scripts/11i_serve_model:modelD
  ```
  e invia un PNG (vedi `11j_generate_mnist_image.py`).
