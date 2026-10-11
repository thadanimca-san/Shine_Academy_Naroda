"""Puts diagram blocks into a chapter.json, next to the theory they illustrate.

Each figure is a dict:
  {"id": "s3.fig1", "after": "s3.thm", "file": "fig_x.png",
   "title": (en, hi, gu), "body": (en, hi, gu)}
Running it again replaces the same blocks, so captions can be edited and re-run.
"""
import json
import os


def insert_figures(chapter_dir, figures):
    path = os.path.join(chapter_dir, "chapter.json")
    chapter = json.load(open(path, encoding="utf-8"))
    prefix = chapter["sections"][0]["blocks"][0]["id"].split(".")[0]
    for fig in figures:
        if not os.path.exists(os.path.join(chapter_dir, fig["file"])):
            raise FileNotFoundError(f"{chapter_dir}/{fig['file']}")
        block_id = f"{prefix}.{fig['id']}"
        block = {"id": block_id, "type": "diagram", "title": fig["title"][0], "body": fig["body"][0],
                 "image_url": f"{chapter_dir.rstrip('/')}/{fig['file']}"}
        for i, lang in ((1, "hi"), (2, "gu")):
            block[f"title_{lang}"] = fig["title"][i]
            block[f"body_{lang}"] = fig["body"][i]
        section_id = fig["id"].split(".")[0]
        section = next(s for s in chapter["sections"] if s["id"] == section_id)
        blocks = [b for b in section["blocks"] if b["id"] != block_id]
        anchor = f"{prefix}.{fig['after']}"
        at = next(i for i, b in enumerate(blocks) if b["id"] == anchor) + 1
        blocks.insert(at, block)
        section["blocks"] = blocks
    with open(path, "w", encoding="utf-8") as out:
        json.dump(chapter, out, ensure_ascii=False, indent=2)
        out.write("\n")
    print(f"{len(figures)} figures in {path}")
