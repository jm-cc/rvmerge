import argparse
import pikepdf


def parse_args():
    parser = argparse.ArgumentParser(description="RVmerge", prog="rvmerge")
    parser.add_argument("recto", help="PDF containing recto pages")
    parser.add_argument("verso", help="PDF containing verso pages")
    parser.add_argument("output", help="output file")
    return parser.parse_args()


def merge_pdf(recto, verso):
    output = pikepdf.new()
    num_pages = len(recto.pages)
    num_pages_verso = len(verso.pages)
    for i in range(num_pages):
        output.pages.append(recto.pages[i])
        if i < num_pages_verso:
            output.pages.append(verso.pages[num_pages_verso - i - 1])
    return output


def main():
    args = parse_args()
    with pikepdf.open(args.recto) as recto:
        with pikepdf.open(args.verso) as verso:
            final = merge_pdf(recto, verso)
    final.save(args.output)
    final.close()


if __name__ == "__main__":
    main()
