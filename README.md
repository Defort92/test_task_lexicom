# test_task_lexicom


## Второе задание
```
CREATE INDEX idx_short_names_name ON short_names(name);
CREATE INDEX idx_full_names_name_without_extension ON full_names ((split_part(name, '.', 1)));

UPDATE full_names f
SET status = s.status
FROM short_names s
WHERE split_part(f.name, '.', 1) = s.name;
```
