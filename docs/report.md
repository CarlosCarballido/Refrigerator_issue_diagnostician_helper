# Report

## Truth Tables

### 1. Nodo: `Refrigerator Doesn't Cool`

| Incorrect Internal Temperature | Refrigerator Doesn't Cool = True | Refrigerator Doesn't Cool = False |
|--------------------------------|----------------------------------|-----------------------------------|
| True                           | 0.85                             | 0.15                              |
| False                          | 0.2                              | 0.8                               |

### 2. Nodo: `Light Not Turning On`

| Incorrect Voltage | Light Not Turning On = True | Light Not Turning On = False |
|-------------------|-----------------------------|------------------------------|
| True              | 0.6                         | 0.4                          |
| False             | 0.1                         | 0.9                          |

### 3. Nodo: `Refrigerator Doesn't Stop`

| Incorrect Voltage | Compressor Failure | Refrigerator Doesn't Stop = True | Refrigerator Doesn't Stop = False |
|-------------------|--------------------|----------------------------------|-----------------------------------|
| True              | True               | 0.7                              | 0.3                               |
| True              | False              | 0.5                              | 0.5                               |
| False             | True               | 0.6                              | 0.4                               |
| False             | False              | 0.1                              | 0.9                               |

### 4. Nodo: `Incorrect Internal Temperature`

| Door Doesn't Lock | Dirt | Incorrect Fan Speed | Incorrect Internal Temperature = True | Incorrect Internal Temperature = False |
|-------------------|------|---------------------|--------------------------------------|---------------------------------------|
| True              | True | True                | 0.9                                   | 0.1                                    |
| True              | True | False               | 0.8                                   | 0.2                                    |
| True              | False| True                | 0.7                                   | 0.3                                    |
| True              | False| False               | 0.5                                   | 0.5                                    |
| False             | True | True                | 0.7                                   | 0.3                                    |
| False             | True | False               | 0.6                                   | 0.4                                    |
| False             | False| True                | 0.4                                   | 0.6                                    |
| False             | False| False               | 0.2                                   | 0.8                                    |

### 5. Nodo: `Incorrect Voltage`

| Incorrect Coolant Pressure | Incorrect Voltage = True | Incorrect Voltage = False |
|----------------------------|--------------------------|---------------------------|
| True                       | 0.7                      | 0.3                       |
| False                      | 0.2                      | 0.8                       |

### 6. Nodo: `Compressor Failure`

| Dirt | Compressor Failure = True | Compressor Failure = False |
|------|---------------------------|----------------------------|
| True | 0.26                      | 0.74                       |
| False| 0.1                       | 0.9                        |
