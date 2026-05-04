import json
from stockfish import Stockfish
from chess960 import generate_chess960_backranks, backrank_to_fen
from pawn_support import position_has_unsupported_pawn

RESULT_FILE = "chess960_results.json"

try:
    with open(RESULT_FILE, "r") as f:
        results = json.load(f)
except:
    results = {}

all_backranks = generate_chess960_backranks()

fully_defended = [
    i for i, br in enumerate(all_backranks)
    if not position_has_unsupported_pawn(br)
]

non_balanced = [i for i in range(960) if i not in fully_defended]

engine = Stockfish(depth=18)

done = set(int(k) for k in results.keys())
remaining = [i for i in non_balanced if i not in done]

batch = remaining[:100]

print(f"Evaluating next {len(batch)} positions...")

for idx in batch:
    br = all_backranks[idx]
    fen = backrank_to_fen(br)

    engine.set_fen_position(fen)
    score = engine.get_evaluation()

    val = score["value"] if score["type"] == "cp" else None

    results[str(idx)] = {
        "backrank": br,
        "fen": fen,
        "eval": val
    }

    with open(RESULT_FILE, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Saved {idx} ({len(results)}/{len(non_balanced)})")

print("Batch complete!")
print(f"Total evaluated so far: {len(results)} / {len(non_balanced)}")
