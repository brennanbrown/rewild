"""Tests for the Rewild Journal CLI.

These focus on the pure functions so they can run non-interactively in CI.
"""

from datetime import datetime
from pathlib import Path

from cli.rewild_journal.cli import (
  JournalEntry,
  build_markdown,
  parse_args,
  save_entry,
  slugify_name,
)


def make_sample_entry() -> JournalEntry:
  """Construct a minimal, valid JournalEntry for testing."""

  now = datetime(2025, 12, 3, 18, 30)
  return JournalEntry(
    student="Brennan Kenneth Brown",
    course="Creative Writing 101",
    practice="Freewriting as Rewilding",
    location="Indoor classroom",
    weather="Overcast",
    created_at=now,
    presences="Trees, crows",
    senses="Rustling leaves",
    freewrite="This is a test entry.",
  )


def test_slugify_name_basic():
  assert slugify_name("Brennan Kenneth Brown") == "brennan-kenneth-brown"


def test_slugify_name_empty_falls_back_to_student():
  assert slugify_name("") == "student"


def test_build_markdown_contains_expected_sections():
  entry = make_sample_entry()
  markdown = build_markdown(entry)

  assert "student: Brennan Kenneth Brown" in markdown
  assert "# Rewild Journal Entry" in markdown
  assert "## More-than-human presences" in markdown
  assert "## Sensory notes" in markdown
  assert "## Freewriting" in markdown


def test_save_entry_creates_file(tmp_path):
  entry = make_sample_entry()
  output_dir = tmp_path / "journals"

  target = save_entry(entry, output_dir)

  assert target.exists()
  text = target.read_text(encoding="utf-8")
  assert "# Rewild Journal Entry" in text


def test_parse_args_defaults_to_journals_dir():
  args = parse_args([])
  assert isinstance(args.output_dir, Path)
  assert args.output_dir == Path("journals")


def test_parse_args_accepts_custom_output_dir():
  args = parse_args(["--output-dir", "my-journals"])
  assert args.output_dir == Path("my-journals")
