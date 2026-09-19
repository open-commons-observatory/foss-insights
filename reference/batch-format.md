# Batch format

A batch is a text file (`batches/NNNN-name.tsv`, UTF-8), one line per record or per group of records:

```
ref[,ref...] | classes | tags | summary
```

| column | rules |
|---|---|
| `ref` | one or more refs separated by commas: `i1836`, `c66fda2c`, `z2i75`, `z2c1a2b3c`. Records sharing a line receive identical tags and summary. |
| `classes` | comma list of class ids from `taxonomy/classes.json`, or `-`. Classes are **added** (union with existing). A leading `~` (for example `~O1`) marks an **inferred** class, stored in `classes_inferred`. An unknown class rejects the batch. |
| `tags` | space-separated `facet:value` tokens. A facet mentioned here **replaces** that facet's previous values. Values must exist in `facets.json`; a single-valued facet takes one value. Extra tokens: `status=read|analyzed`, `depth=title|thread|full|source`. |
| `summary` | optional. Replaces the summary. If it starts with `+ ` it is **appended** (idempotent: an identical clause is not added twice). Empty: unchanged. |

Comment lines start with `#` (use them for the batch's header: the range, the rule, the date). Blank lines are ignored. The summary may contain `|` only as the last column; the split is on the first three pipes.

## Defaults
`status`: `analyzed`. `depth`: `thread` for issues, `title` for commits. Depth and status never move down.

## Atomicity
The tool parses and validates **every line first**. Any error (unknown ref, unknown facet or value, two values for a single-valued facet, unknown class, bad status or depth) prints `BATCH REJECTED (nothing written)` with the line numbers and exits non-zero. Nothing is written until the whole file is valid.

## Archiving
`pz.py apply` copies a batch that lives outside `batches/` to `batches/NNNN-name.tsv` (next number). Batches created inside `batches/` are used in place. `pz.py replay` re-applies all of them in numeric order.

## Examples
```
# issues #12..#40, read in full
i12 | - | kind:question outcome:docs-answer conf:stated depth=full | Asks how to run it; answered from the docs.
i57,i94 | S3 | kind:bug cause:config-error outcome:fixed conf:stated depth=full | Two reports of the same startup failure, fixed in 1.2.
i57 | - | depth=full | + Deep read: the maintainer states the failure needs a kernel newer than 3.10.
c66fda2c,c187affb | - | ctype:fix engine:main | Two small fixes to the option parser.
z2i75 | - | kind:bug cause:memory-bug outcome:fixed conf:stated depth=full | Crash on a 64-bit target; fixed by changing how pointers are stored.
```

## Mistakes the tool catches (and `check` warns about)
A ref with a stray letter (`i1127b`), an unknown class (`D9`), a single-valued facet with two values, and (as warnings) a full summary over an analysed record, a facet line that drops values, and duplicate refs.
