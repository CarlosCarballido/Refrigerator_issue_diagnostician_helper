# Report

# Truth Tables from Bayesian Net

## Nodo 1: `Refrigerator Doesn't Cool`

| Incorrect Internal Temperature | Door Doesn't Lock | Dirt | Incorrect Fan Speed | Refrigerator Doesn't Cool = True | Refrigerator Doesn't Cool = False |
|--------------------------------|-------------------|------|---------------------|----------------------------------|-----------------------------------|
| True                           | True              | True | True                | 0.9                              | 0.1                               |
| True                           | True              | True | False               | 0.85                             | 0.15                              |
| True                           | True              | False| True                | 0.8                              | 0.2                               |
| True                           | True              | False| False               | 0.75                             | 0.25                              |
| True                           | False             | True | True                | 0.8                              | 0.2                               |
| True                           | False             | True | False               | 0.75                             | 0.25                              |
| True                           | False             | False| True                | 0.7                              | 0.3                               |
| True                           | False             | False| False               | 0.6                              | 0.4                               |
| False                          | True              | True | True                | 0.6                              | 0.4                               |
| False                          | True              | True | False               | 0.5                              | 0.5                               |
| False                          | True              | False| True                | 0.4                              | 0.6                               |
| False                          | True              | False| False               | 0.3                              | 0.7                               |
| False                          | False             | True | True                | 0.5                              | 0.5                               |
| False                          | False             | True | False               | 0.4                              | 0.6                               |
| False                          | False             | False| True                | 0.2                              | 0.8                               |
| False                          | False             | False| False               | 0.1                              | 0.9                               |                            |

---


## Nodo 2: `Refrigerator Fills with Frost`

| Incorrect Internal Temperature | Door Doesn't Lock | Dirt | Incorrect Fan Speed | Refrigerator Fills with Frost = True | Refrigerator Fills with Frost = False |
|--------------------------------|-------------------|------|---------------------|--------------------------------------|---------------------------------------|
| True                           | True              | True | True                | 0.9                                  | 0.1                                   |
| True                           | True              | True | False               | 0.85                                 | 0.15                                  |
| True                           | True              | False| True                | 0.8                                  | 0.2                                   |
| True                           | True              | False| False               | 0.75                                 | 0.25                                  |
| True                           | False             | True | True                | 0.8                                  | 0.2                                   |
| True                           | False             | True | False               | 0.75                                 | 0.25                                  |
| True                           | False             | False| True                | 0.7                                  | 0.3                                   |
| True                           | False             | False| False               | 0.6                                  | 0.4                                   |
| False                          | True              | True | True                | 0.6                                  | 0.4                                   |
| False                          | True              | True | False               | 0.5                                  | 0.5                                   |
| False                          | True              | False| True                | 0.4                                  | 0.6                                   |
| False                          | True              | False| False               | 0.3                                  | 0.7                                   |
| False                          | False             | True | True                | 0.5                                  | 0.5                                   |
| False                          | False             | True | False               | 0.4                                  | 0.6                                   |
| False                          | False             | False| True                | 0.3                                  | 0.7                                   |
| False                          | False             | False| False               | 0.2                                  | 0.8                                   |
---

## Nodo 3: `Light Not Turning On`

| Incorrect Voltage | Incorrect Coolant Pressure | Light Not Turning On = True | Light Not Turning On = False |
|-------------------|----------------------------|-----------------------------|------------------------------|
| True              | True                       | 0.7                         | 0.3                          |
| True              | False                      | 0.6                         | 0.4                          |
| False             | True                       | 0.4                         | 0.6                          |
| False             | False                      | 0.1                         | 0.9                          |

---


## Nodo 4: `Refrigerator Doesn't Stop`

| Incorrect Voltage | Compressor Failure | Incorrect Coolant Pressure | Refrigerator Doesn't Stop = True | Refrigerator Doesn't Stop = False |
|-------------------|--------------------|----------------------------|----------------------------------|-----------------------------------|
| True              | True               | True                       | 0.75                             | 0.25                              |
| True              | True               | False                      | 0.6                              | 0.4                               |
| True              | False              | True                       | 0.55                             | 0.45                              |
| True              | False              | False                      | 0.5                              | 0.5                               |
| False             | True               | True                       | 0.65                             | 0.35                              |
| False             | True               | False                      | 0.6                              | 0.4                               |
| False             | False              | True                       | 0.2                              | 0.8                               |
| False             | False              | False                      | 0.1                              | 0.9                               |

---

## 5. Nodo: `Incorrect Internal Temperature`

| Door Doesn't Lock | Dirt | Incorrect Fan Speed | Incorrect Coolant Pressure | Compressor Failure | Incorrect Internal Temperature = True | Incorrect Internal Temperature = False |
|-------------------|------|---------------------|----------------------------|--------------------|--------------------------------------|---------------------------------------|
| True              | True | True                | True                       | True               | 0.95                                 | 0.05                                  |
| True              | True | True                | True                       | False              | 0.9                                  | 0.1                                   |
| True              | True | True                | False                      | True               | 0.85                                 | 0.15                                  |
| True              | True | True                | False                      | False              | 0.8                                  | 0.2                                   |
| True              | True | False               | True                       | True               | 0.85                                 | 0.15                                  |
| True              | True | False               | True                       | False              | 0.8                                  | 0.2                                   |
| True              | True | False               | False                      | True               | 0.75                                 | 0.25                                  |
| True              | True | False               | False                      | False              | 0.7                                  | 0.3                                   |
| True              | False| True                | True                       | True               | 0.8                                  | 0.2                                   |
| True              | False| True                | True                       | False              | 0.75                                 | 0.25                                  |
| True              | False| True                | False                      | True               | 0.7                                  | 0.3                                   |
| True              | False| True                | False                      | False              | 0.5                                  | 0.5                                   |
| True              | False| False               | True                       | True               | 0.7                                  | 0.3                                   |
| True              | False| False               | True                       | False              | 0.6                                  | 0.4                                   |
| True              | False| False               | False                      | True               | 0.5                                  | 0.5                                   |
| True              | False| False               | False                      | False              | 0.3                                  | 0.7                                   |
| False             | True | True                | True                       | True               | 0.8                                  | 0.2                                   |
| False             | True | True                | True                       | False              | 0.7                                  | 0.3                                   |
| False             | True | True                | False                      | True               | 0.6                                  | 0.4                                   |
| False             | True | True                | False                      | False              | 0.4                                  | 0.6                                   |
| False             | True | False               | True                       | True               | 0.6                                  | 0.4                                   |
| False             | True | False               | True                       | False              | 0.5                                  | 0.5                                   |
| False             | True | False               | False                      | True               | 0.4                                  | 0.6                                   |
| False             | True | False               | False                      | False              | 0.2                                  | 0.8                                   |
| False             | False| True                | True                       | True               | 0.5                                  | 0.5                                   |
| False             | False| True                | True                       | False              | 0.4                                  | 0.6                                   |
| False             | False| True                | False                      | True               | 0.3                                  | 0.7                                   |
| False             | False| True                | False                      | False              | 0.1                                  | 0.9                                   |
| False             | False| False               | True                       | True               | 0.3                                  | 0.7                                   |
| False             | False| False               | True                       | False              | 0.2                                  | 0.8                                   |
| False             | False| False               | False                      | True               | 0.1                                  | 0.9                                   |
| False             | False| False               | False                      | False              | 0.05                                 | 0.95                                  |

---


## Nodo 6: `Incorrect Voltage`

| Incorrect Coolant Pressure | Incorrect Voltage = True | Incorrect Voltage = False |
|----------------------------|--------------------------|---------------------------|
| True                       | 0.7                      | 0.3                       |
| False                      | 0.2                      | 0.8                       |
---

## 7. Nodo: `Door Doesn't Lock`

| Door Doesn't Lock = True | Door Doesn't Lock = False |
|--------------------------|---------------------------|
| 0.3                      | 0.7                       |

---

## 8. Nodo: `Dirt`

| Dirt = True | Dirt = False |
|-------------|--------------|
| 0.4         | 0.6          |

---

## 9. Nodo: `Incorrect Fan Speed`

| Incorrect Fan Speed = True | Incorrect Fan Speed = False |
|----------------------------|-----------------------------|
| 0.25                       | 0.75                        |

---

## 10. Nodo: `Incorrect Coolant Pressure`

| Incorrect Coolant Pressure = True | Incorrect Coolant Pressure = False |
|-----------------------------------|------------------------------------|
| 0.2                               | 0.8                                |

---

## 11. Nodo: `Compressor Failure`

| Compressor Failure = True | Compressor Failure = False |
|---------------------------|----------------------------|
| 0.15                      | 0.85                       |