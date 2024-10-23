# Report

## Truth Tables

### 1. Nodo: `No Cooling`

| Compressor Failure | Door Not Closing | No Cooling = True | No Cooling = False |
|--------------------|------------------|-------------------|--------------------|
| True               | True             | 0.9               | 0.1                |
| True               | False            | 0.8               | 0.2                |
| False              | True             | 0.7               | 0.3                |
| False              | False            | 0.1               | 0.9                |

### 2. Nodo: `Lighting Issue`

| Voltage Issue | Lighting Issue = True | Lighting Issue = False |
|---------------|-----------------------|------------------------|
| True          | 0.38                  | 0.62                   |
| False         | 0.1                   | 0.9                    |

### 3. Nodo: `Compressor Failure`

| Dirt | Compressor Failure = True | Compressor Failure = False |
|------|---------------------------|----------------------------|
| True | 0.3                       | 0.7                        |
| False| 0.1                       | 0.9                        |

### 4. Nodo: `Door Not Closing`

| Defective Door Lock | Dirt | Door Not Closing = True | Door Not Closing = False |
|---------------------|------|------------------------|-------------------------|
| True                | True | 0.8                    | 0.2                     |
| True                | False| 0.6                    | 0.4                     |
| False               | True | 0.4                    | 0.6                     |
| False               | False| 0.2                    | 0.8                     |

### 5. Nodo: `Temperature Fluctuations`

| Compressor Failure | Temperature Sensor | Temperature Fluctuations = True | Temperature Fluctuations = False |
|--------------------|--------------------|--------------------------------|---------------------------------|
| True               | True               | 0.8                            | 0.2                             |
| True               | False              | 0.7                            | 0.3                             |
| False              | True               | 0.6                            | 0.4                             |
| False              | False              | 0.1                            | 0.9                             |

### 6. Nodo: `Fridge Not Stopping`

| Compressor Failure | Fridge Not Stopping = True | Fridge Not Stopping = False |
|--------------------|---------------------------|----------------------------|
| True               | 0.7                       | 0.3                        |
| False              | 0.2                       | 0.8                        |

### 7. Nodo: `Fridge Not Sealing`

| Door Not Closing | Fridge Not Sealing = True | Fridge Not Sealing = False |
|------------------|--------------------------|---------------------------|
| True             | 0.8                      | 0.2                       |
| False            | 0.2                      | 0.8                       |
