import json, sys, os

TEMPLATE_FILE = "Cultural_Map_Template.html"

def load_template(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def fill_template(template, data):
    payload = json.dumps(data, ensure_ascii=False, indent=2)
    return template.replace("/*__DATA__*/", payload)

def main():
    if len(sys.argv) < 2:
        print("Usage: python cultural_map_batch_generator.py clients.json")
        sys.exit(1)
    template = load_template(TEMPLATE_FILE)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        cfg = json.load(f)
    out_dir = cfg.get("out_dir", ".")
    os.makedirs(out_dir, exist_ok=True)
    for client in cfg.get("clients", []):
        fname = client.get("file_name") or "Cultural_Map.html"
        html = fill_template(template, client)
        out_path = os.path.join(out_dir, fname)
        with open(out_path, "w", encoding="utf-8") as outf:
            outf.write(html)
        print("Wrote", out_path)

if __name__ == "__main__":
    main()