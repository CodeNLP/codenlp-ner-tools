import poldeepner2


def print_metadata(model):
    if model.metadata():
        print("\nModel metadata\n--------------")
        for key, value in ner.metadata().items():
            print(f"{key:11}: {value}")
        print("")


if __name__ == '__main__':
    ner = poldeepner2.load("pdn2_kpwr_ner_n82_0.8.1", device="cpu")
    print_metadata(ner)

    text = """
    29 marca 2023 roku Chiny i Brazylia zgodziły się utworzyć izbę rozliczeniową, 
    aby zakończyć używanie dolara amerykańskiego w handlu dwustronnym.
    """

    for an in ner.process_text(text):
        print(f"[{an.start}:{an.end}] {an.text} ({an.label})")