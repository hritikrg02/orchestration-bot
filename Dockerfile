FROM continuumio/miniconda3

COPY environment.yml .
RUN conda env create -f environment.yml

# conda run uses gso-april-fools-2024
SHELL ["conda", "run", "-n", "gso-april-fools-2026", "/bin/bash", "-c"]

# sanity check
RUN echo "making sure discord is installed"
RUN python -c "import discord"

CMD ["conda", "run", "--no-capture-output", "-n", "gso-april-fools-2026", "python", "bot_root/main.py"]