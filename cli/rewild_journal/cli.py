#!/usr/bin/env python3

"""Rewild Journal CLI

An experimental terminal prompt for students to capture place-based journal
entries as markdown files. Prompts are loosely aligned with the Nature-as-Text
and Ecology of Mind strands.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class JournalEntry:
  """A single journal entry collected from a student."""

  student: str
  course: str
  practice: str
  location: str
  weather: str
  created_at: datetime
  presences: str
  senses: str
  freewrite: str


def prompt_nonempty(message: str) -> str:
  """Prompt until a non-empty response is provided."""

  while True:
    value = input(message).strip()
    if value:
      return value


def prompt_optional(message: str) -> str:
  """Prompt once; return the (possibly empty) response."""

  return input(message).strip()


def collect_multiline(intro: str) -> str:
  """Collect multi-line input until a single '.' line or EOF.

  This keeps things simple: type until done, then enter a single period
  `.` on its own line.
  """

  print("\n" + intro)
  print("(Type your notes. When you're finished, enter a single '.' on its own line.)")

  lines: list[str] = []
  while True:
    try:
      line = input()
    except EOFError:
      break
    if line.strip() == ".":
      break
    lines.append(line)

  return "\n".join(lines).strip()


def slugify_name(name: str) -> str:
  """Create a safe slug from a student's name for filenames."""

  base = name.lower().strip().replace(" ", "-") or "student"
  safe = [c for c in base if c.isalnum() or c in {"-", "_"}]
  return "".join(safe) or "student"


def build_markdown(entry: JournalEntry) -> str:
  """Assemble the markdown content for a journal entry."""

  timestamp_human = entry.created_at.strftime("%Y-%m-%d %H:%M")

  front_matter = [
    "---",
    f"student: {entry.student}",
    f"course: {entry.course}" if entry.course else "course: ",
    f"practice: {entry.practice}" if entry.practice else "practice: ",
    f"location: {entry.location}" if entry.location else "location: ",
    f"weather: {entry.weather}" if entry.weather else "weather: ",
    f"created_at: {timestamp_human}",
    "---",
    "",
  ]

  body: list[str] = []
  body.append("# Today's Rewild Journal Entry")
  body.append("")

  body.append("## More-than-human Presences")
  body.append("")
  body.append(entry.presences or "_(no entries)_")
  body.append("")

  body.append("## Sensory Notes")
  body.append("")
  body.append(entry.senses or "_(no entries)_")
  body.append("")

  body.append("## Freewriting")
  body.append("")
  body.append(entry.freewrite or "_(no entries)_")
  body.append("")

  return "\n".join(front_matter + body)


def collect_entry() -> JournalEntry:
  """Run the interactive prompts and return a populated JournalEntry."""

  print("=== Rewild Journal CLI ===")
  print("=== created by Brennan Kenneth Brown ===")
  print("This experimental prompt will save your responses as a markdown journal entry.\n")

  student = prompt_nonempty("Your name: ")
  course = prompt_optional("Course / group (optional): ")
  practice = prompt_optional("Practice or prompt name (e.g. Field Journal, Freewriting): ")
  location = prompt_optional("Where are you right now? ")
  weather = prompt_optional("Weather / atmosphere (optional): ")

  presences = collect_multiline("List more-than-human presences you notice (one per line):")
  senses = collect_multiline(
    "Note any sensory details (sounds, textures, temperatures, smells, light/shadow. etc.):"
  )
  freewrite = collect_multiline("Freewrite about this moment and place, or about anything, really:")

  now = datetime.now()

  return JournalEntry(
    student=student,
    course=course,
    practice=practice,
    location=location,
    weather=weather,
    created_at=now,
    presences=presences,
    senses=senses,
    freewrite=freewrite,
  )


def save_entry(entry: JournalEntry, output_dir: Path) -> Path:
  """Save a journal entry to the given directory and return the file path."""

  output_dir.mkdir(parents=True, exist_ok=True)

  slug = slugify_name(entry.student)
  timestamp_slug = entry.created_at.strftime("%Y%m%d-%H%M%S")
  filename = f"{timestamp_slug}-{slug}.md"

  markdown = build_markdown(entry)
  target = output_dir / filename
  target.write_text(markdown, encoding="utf-8")
  return target


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
  """Parse command-line arguments."""

  parser = argparse.ArgumentParser(description="Rewild Journal CLI")
  parser.add_argument(
    "--output-dir",
    type=Path,
    default=Path("journals"),
    help="Directory to store journal markdown files (default: ./journals)",
  )
  return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> None:
  """Entry point for the CLI."""

  args = parse_args(argv)
  entry = collect_entry()

  try:
    target = save_entry(entry, args.output_dir)
  except OSError as exc:
    print(f"Error saving journal entry: {exc}")
    return

  base_dir = Path.cwd()
  try:
    rel = target.relative_to(base_dir)
  except ValueError:
    rel = target

  print(f"\nSaved journal to {rel}")
  print("You can commit this file with your project or share it as part of your portfolio. Enjoy!\n")


if __name__ == "__main__":  # pragma: no cover - direct CLI execution
  try:
    main()
  except KeyboardInterrupt:
    print("\nInterrupted. No journal saved.")
