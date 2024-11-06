# Truth Tables from Bayesian Net

## Nodo 1: `Refrigerator Doesn't Cool`

### Nodo: Refrigerator Doesn't Cool

| Incorrect Internal Temperature | Door Doesn't Lock | Dirt | Incorrect Fan Speed | Incorrect Voltage | Incorrect Coolant Pressure | Compressor Failure | Refrigerator Doesn't Cool = True | Refrigerator Doesn't Cool = False |
|--------------------------------|-------------------|------|---------------------|-------------------|----------------------------|---------------------|----------------------------------|-----------------------------------|
| True                           | True              | True | True                | True              | True                       | True                | 0.53                             | 0.47               |
| True                           | True              | True | True                | True              | True                       | False               | 0.99                             | 0.01               |
| True                           | True              | True | True                | True              | False                      | True                | 0.27                             | 0.73               |
| True                           | True              | True | True                | True              | False                      | False               | 0.22                             | 0.78               |
| True                           | True              | True | True                | False             | True                       | True                | 0.03                             | 0.97               |
| True                           | True              | True | True                | False             | True                       | False               | 0.61                             | 0.39               |
| True                           | True              | True | True                | False             | False                      | True                | 0.76                             | 0.24               |
| True                           | True              | True | True                | False             | False                      | False               | 0.56                             | 0.44               |
| True                           | True              | True | False               | True              | True                       | True                | 0.57                             | 0.43               |
| True                           | True              | True | False               | True              | True                       | False               | 0.22                             | 0.78               |
| True                           | True              | True | False               | True              | False                      | True                | 0.8                              | 0.2                |
| True                           | True              | True | False               | True              | False                      | False               | 0.25                             | 0.75               |
| True                           | True              | True | False               | False             | True                       | True                | 0.82                             | 0.18               |
| True                           | True              | True | False               | False             | True                       | False               | 0.61                             | 0.39               |
| True                           | True              | True | False               | False             | False                      | True                | 0.78                             | 0.22               |
| True                           | True              | True | False               | False             | False                      | False               | 0.16                             | 0.84               |
| True                           | True              | False | True               | True              | True                       | True                | 0.46                             | 0.54               |
| True                           | True              | False | True               | True              | True                       | False               | 0.68                             | 0.32               |
| True                           | True              | False | True               | True              | False                      | True                | 0.36                             | 0.64               |
| True                           | True              | False | True               | True              | False                      | False               | 0.62                             | 0.38               |
| True                           | True              | False | True               | False             | True                       | True                | 0.81                             | 0.19               |
| True                           | True              | False | True               | False             | True                       | False               | 0.07                             | 0.93               |
| True                           | True              | False | True               | False             | False                      | True                | 0.7                              | 0.3                |
| True                           | True              | False | True               | False             | False                      | False               | 0.91                             | 0.09               |
| True                           | True              | False | False                  | True              | True                       | True                | 0.19                             | 0.81               |
| True                           | True              | False | False                  | True              | True                       | False               | 0.74                             | 0.26               |
| True                           | True              | False | False                  | True              | False                      | True                | 0.78                             | 0.22               |
| True                           | True              | False | False                  | True              | False                      | False               | 0.94                             | 0.06               |
| True                           | True              | False | False                  | False             | True                       | True                | 0.04                             | 0.96               |
| True                           | True              | False | False                  | False             | True                       | False               | 0.72                             | 0.28               |
| True                           | True              | False | False                  | False             | False                      | True                | 0.53                             | 0.47               |
| True                           | True              | False | False                  | False             | False                      | False               | 0.25                             | 0.75               |
| True                           | False                 | True | True                | True              | True                       | True                | 0.71                             | 0.29               |
| True                           | False                 | True | True                | True              | True                       | False               | 0.81                             | 0.19               |
| True                           | False                 | True | True                | True              | False                      | True                | 0.41                             | 0.59               |
| True                           | False                 | True | True                | True              | False                      | False               | 0.47                             | 0.53               |
| True                           | False                 | True | True                | False             | True                       | True                | 0.68                             | 0.32               |
| True                           | False                 | True | True                | False             | True                       | False               | 0.19                             | 0.81               |
| True                           | False                 | True | True                | False             | False                      | True                | 0.94                             | 0.06               |
| True                           | False                 | True | True                | False             | False                      | False               | 0.93                             | 0.07               |
| True                           | False                 | True | False               | True              | True                       | True                | 0.06                             | 0.94               |
| True                           | False                 | True | False               | True              | True                       | False               | 0.05                             | 0.95               |
| True                           | False                 | True | False               | True              | False                      | True                | 0.13                             | 0.87               |
| True                           | False                 | True | False               | True              | False                      | False               | 0.17                             | 0.83               |
| True                           | False                 | True | False               | False             | True                       | True                | 0.69                             | 0.31               |
| True                           | False                 | True | False               | False             | True                       | False               | 0.35                             | 0.65               |
| True                           | False                 | True | False               | False             | False                      | True                | 0.85                             | 0.15               |
| True                           | False                 | True | False               | False             | False                      | False               | 0.9                              | 0.1                |
| True                           | False                 | False | True               | True              | True                       | True                | 0.44                             | 0.56               |
| True                           | False                 | False | True               | True              | True                       | False               | 0.25                             | 0.75               |
| True                           | False                 | False | True               | True              | False                      | True                | 0.63                             | 0.37               |
| True                           | False                 | False | True               | True              | False                      | False               | 0.64                             | 0.36               |
| True                           | False                 | False | True               | False             | True                       | True                | 0.28                             | 0.72               |
| True                           | False                 | False | True               | False             | True                       | False               | 0.35                             | 0.65               |
| True                           | False                 | False | True               | False             | False                      | True                | 0.63                             | 0.37               |
| True                           | False                 | False | True               | False             | False                      | False               | 0.53                             | 0.47               |
| True                           | False                 | False | False                  | True              | True                       | True                | 0.23                             | 0.77               |
| True                           | False                 | False | False                  | True              | True                       | False               | 0.83                             | 0.17               |
| True                           | False                 | False | False                  | True              | False                      | True                | 0.09                             | 0.91               |
| True                           | False                 | False | False                  | True              | False                      | False               | 0.39                             | 0.61               |
| True                           | False                 | False | False                  | False             | True                       | True                | 0.76                             | 0.24               |
| True                           | False                 | False | False                  | False             | True                       | False               | 0.24                             | 0.76               |
| True                           | False                 | False | False                  | False             | False                      | True                | 0.41                             | 0.59               |
| True                           | False                 | False | False                  | False             | False                      | False               | 0.18                             | 0.82               |
| False                           | True                 | True | True                | True              | True                       | True                | 0.18                             | 0.82               |
| False                           | True                 | True | True                | True              | True                       | False               | 0.82                             | 0.18               |
| False                           | True                 | True | True                | True              | False                      | True                | 0.48                             | 0.52               |
| False                           | True                 | True | True                | True              | False                      | False               | 0.08                             | 0.92               |
| False                           | True                 | True | True                | False             | True                       | True                | 0.03                             | 0.97               |
| False                           | True                 | True | True                | False             | True                       | False               | 0.57                             | 0.43               |
| False                           | True                 | True | True                | False             | False                      | True                | 0.76                             | 0.24               |
| False                           | True                 | True | True                | False             | False                      | False               | 0.64                             | 0.36               |
| False                           | True                 | True | False               | True              | True                       | True                | 0.31                             | 0.69               |
| False                           | True                 | True | False               | True              | True                       | False               | 0.2                              | 0.8                |
| False                           | True                 | True | False               | True              | False                      | True                | 0.15                             | 0.85               |
| False                           | True                 | True | False               | True              | False                      | False               | 0.44                             | 0.56               |
| False                           | True                 | True | False               | False             | True                       | True                | 0.02                             | 0.98               |
| False                           | True                 | True | False               | False             | True                       | False               | 0.17                             | 0.83               |
| False                           | True                 | True | False               | False             | False                      | True                | 0.96                             | 0.04               |
| False                           | True                 | True | False               | False             | False                      | False               | 0.57                             | 0.43               |
| False                           | True                 | False | True               | True              | True                       | True                | 0.25                             | 0.75               |
| False                           | True                 | False | True               | True              | True                       | False               | 0.41                             | 0.59               |
| False                           | True                 | False | True               | True              | False                      | True                | 0.3                              | 0.7                |
| False                           | True                 | False | True               | True              | False                      | False               | 0.71                             | 0.29               |
| False                           | True                 | False | True               | False             | True                       | True                | 0.28                             | 0.72               |
| False                           | True                 | False | True               | False             | True                       | False               | 0.87                             | 0.13               |
| False                           | True                 | False | True               | False             | False                      | True                | 0.81                             | 0.19               |
| False                           | True                 | False | True               | False             | False                      | False               | 0.14                             | 0.86               |
| False                           | True                 | False | False                  | True              | True                       | True                | 0.19                             | 0.81               |
| False                           | True                 | False | False                  | True              | True                       | False               | 0.77                             | 0.23               |
| False                           | True                 | False | False                  | True              | False                      | True                | 0.65                             | 0.35               |
| False                           | True                 | False | False                  | True              | False                      | False               | 0.01                             | 0.99               |
| False                           | True                 | False | False                  | False             | True                       | True                | 0.73                             | 0.27               |
| False                           | True                 | False | False                  | False             | True                       | False               | 0.26                             | 0.74               |
| False                           | True                 | False | False                  | False             | False                      | True                | 0.38                             | 0.62               |
| False                           | True                 | False | False                  | False             | False                      | False               | 0.27                             | 0.73               |
| False                           | False                | True | True                | True              | True                       | True                | 0.39                             | 0.61               |
| False                           | False                | True | True                | True              | True                       | False               | 0.05                             | 0.95               |
| False                           | False                | True | True                | True              | False                      | True                | 0.03                             | 0.97               |
| False                           | False                | True | True                | True              | False                      | False               | 0.42                             | 0.58               |
| False                           | False                | True | True                | False             | True                       | True                | 0.34                             | 0.66               |
| False                           | False                | True | True                | False             | True                       | False               | 0.44                             | 0.56               |
| False                           | False                | True | True                | False             | False                      | True                | 0.9                              | 0.1                |
| False                           | False                | True | True                | False             | False                      | False               | 0.7                              | 0.3                |
| False                           | False                | True | False               | True              | True                       | True                | 0.51                             | 0.49               |
| False                           | False                | True | False               | True              | True                       | False               | 0.13                             | 0.87               |
| False                           | False                | True | False               | True              | False                      | True                | 0.83                             | 0.17               |
| False                           | False                | True | False               | True              | False                      | False               | 0.13                             | 0.87               |
| False                           | False                | True | False               | False             | True                       | True                | 0.9                              | 0.1                |
| False                           | False                | True | False               | False             | True                       | False               | 0.99                             | 0.01               |
| False                           | False                | True | False               | False             | False                      | True                | 0.9                              | 0.1                |
| False                           | False                | True | False               | False             | False                      | False               | 0.62                             | 0.38               |
| False                           | False                | False | True               | True              | True                       | True                | 0.33                             | 0.67               |
| False                           | False                | False | True               | True              | True                       | False               | 0.63                             | 0.37               |
| False                           | False                | False | True               | True              | False                      | True                | 0.33                             | 0.67               |
| False                           | False                | False | True               | True              | False                      | False               | 1.0                              | 0.0                |
| False                           | False                | False | True               | False             | True                       | True                | 0.56                             | 0.44               |
| False                           | False                | False | True               | False             | True                       | False               | 0.55                             | 0.45               |
| False                           | False                | False | True               | False             | False                      | True                | 0.77                             | 0.23               |
| False                           | False                | False | True               | False             | False                      | False               | 0.15                             | 0.85               |
| False                           | False                | False | False                  | True              | True                       | True                | 0.04                             | 0.96               |
| False                           | False                | False | False                  | True              | True                       | False               | 0.55                             | 0.45               |
| False                           | False                | False | False                  | True              | False                      | True                | 0.46                             | 0.54               |
| False                           | False                | False | False                  | True              | False                      | False               | 0.87                             | 0.13               |
| False                           | False                | False | False                  | False             | True                       | True                | 0.29                             | 0.71               |
| False                           | False                | False | False                  | False             | True                       | False               | 0.93                             | 0.07               |
| False                           | False                | False | False                  | False             | False                      | True                | 0.07                             | 0.93               |
| False                           | False                | False | False                  | False             | False                      | False               | 0.73                             | 0.27               |

---

## Nodo 2: `Refrigerator Fills with Frost`

| Incorrect Internal Temperature | Door Doesn't Lock | Dirt | Incorrect Fan Speed | Incorrect Voltage | Incorrect Coolant Pressure | Compressor Failure | Refrigerator Fills with Frost = True | Refrigerator Fills with Frost = False |
|--------------------------------|-------------------|------|---------------------|-------------------|----------------------------|---------------------|--------------------------------------|---------------------------------------|
| True | True | True | True | True | True | True | 0.91 | 0.09 |
| True | True | True | True | True | True | False | 0.97 | 0.03 |
| True | True | True | True | True | False | True | 0.71 | 0.29 |
| True | True | True | True | True | False | False | 0.14 | 0.86 |
| True | True | True | True | False | True | True | 0.21 | 0.79 |
| True | True | True | True | False | True | False | 0.06 | 0.94 |
| True | True | True | True | False | False | True | 0.31 | 0.69 |
| True | True | True | True | False | False | False | 0.45 | 0.55 |
| True | True | True | False | True | True | True | 0.67 | 0.33 |
| True | True | True | False | True | True | False | 0.67 | 0.33 |
| True | True | True | False | True | False | True | 0.83 | 0.17 |
| True | True | True | False | True | False | False | 0.09 | 0.91 |
| True | True | True | False | False | True | True | 0.6 | 0.4 |
| True | True | True | False | False | True | False | 0.71 | 0.29 |
| True | True | True | False | False | False | True | 0.16 | 0.84 |
| True | True | True | False | False | False | False | 0.74 | 0.26 |
| True | True | False | True | True | True | True | 0.26 | 0.74 |
| True | True | False | True | True | True | False | 0.2 | 0.8 |
| True | True | False | True | True | False | True | 0.35 | 0.65 |
| True | True | False | True | True | False | False | 0.28 | 0.72 |
| True | True | False | True | False | True | True | 0.53 | 0.47 |
| True | True | False | True | False | True | False | 0.59 | 0.41 |
| True | True | False | True | False | False | True | 0.99 | 0.01 |
| True | True | False | True | False | False | False | 0.4 | 0.6 |
| True | True | False | False | True | True | True | 0.46 | 0.54 |
| True | True | False | False | True | True | False | 0.1 | 0.9 |
| True | True | False | False | True | False | True | 0.84 | 0.16 |
| True | True | False | False | True | False | False | 0.49 | 0.51 |
| True | True | False | False | False | True | True | 0.15 | 0.85 |
| True | True | False | False | False | True | False | 0.38 | 0.62 |
| True | True | False | False | False | False | True | 0.65 | 0.35 |
| True | True | False | False | False | False | False | 0.48 | 0.52 |
| True | False | True | True | True | True | True | 0.33 | 0.67 |
| True | False | True | True | True | True | False | 0.91 | 0.09 |
| True | False | True | True | True | False | True | 0.12 | 0.88 |
| True | False | True | True | True | False | False | 0.04 | 0.96 |
| True | False | True | True | False | True | True | 0.55 | 0.45 |
| True | False | True | True | False | True | False | 0.84 | 0.16 |
| True | False | True | True | False | False | True | 0.3 | 0.7 |
| True | False | True | True | False | False | False | 0.96 | 0.04 |
| True | False | True | False | True | True | True | 0.78 | 0.22 |
| True | False | True | False | True | True | False | 0.53 | 0.47 |
| True | False | True | False | True | False | True | 0.45 | 0.55 |
| True | False | True | False | True | False | False | 0.59 | 0.41 |
| True | False | True | False | False | True | True | 0.71 | 0.29 |
| True | False | True | False | False | True | False | 0.94 | 0.06 |
| True | False | True | False | False | False | True | 0.86 | 0.14 |
| True | False | True | False | False | False | False | 0.8 | 0.2 |
| True | False | False | True | True | True | True | 0.57 | 0.43 |
| True | False | False | True | True | True | False | 0.83 | 0.17 |
| True | False | False | True | True | False | True | 0.59 | 0.41 |
| True | False | False | True | True | False | False | 0.52 | 0.48 |
| True | False | False | True | False | True | True | 0.26 | 0.74 |
| True | False | False | True | False | True | False | 0.54 | 0.46 |
| True | False | False | True | False | False | True | 0.69 | 0.31 |
| True | False | False | True | False | False | False | 0.72 | 0.28 |
| True | False | False | False | True | True | True | 0.26 | 0.74 |
| True | False | False | False | True | True | False | 0.07 | 0.93 |
| True | False | False | False | True | False | True | 0.72 | 0.28 |
| True | False | False | False | True | False | False | 0.2 | 0.8 |
| True | False | False | False | False | True | True | 0.47 | 0.53 |
| True | False | False | False | False | True | False | 0.28 | 0.72 |
| True | False | False | False | False | False | True | 0.23 | 0.77 |
| True | False | False | False | False | False | False | 0.75 | 0.25 |
| False | True | True | True | True | True | True | 0.99 | 0.01 |
| False | True | True | True | True | True | False | 0.89 | 0.11 |
| False | True | True | True | True | False | True | 0.8 | 0.2 |
| False | True | True | True | True | False | False | 0.14 | 0.86 |
| False | True | True | True | False | True | True | 0.69 | 0.31 |
| False | True | True | True | False | True | False | 0.64 | 0.36 |
| False | True | True | True | False | False | True | 0.69 | 0.31 |
| False | True | True | True | False | False | False | 0.87 | 0.13 |
| False | True | True | False | True | True | True | 0.49 | 0.51 |
| False | True | True | False | True | True | False | 1.0 | 0.0 |
| False | True | True | False | True | False | True | 0.57 | 0.43 |
| False | True | True | False | True | False | False | 0.86 | 0.14 |
| False | True | True | False | False | True | True | 0.31 | 0.69 |
| False | True | True | False | False | True | False | 0.39 | 0.61 |
| False | True | True | False | False | False | True | 0.62 | 0.38 |
| False | True | True | False | False | False | False | 0.29 | 0.71 |
| False | True | False | True | True | True | True | 0.36 | 0.64 |
| False | True | False | True | True | True | False | 0.44 | 0.56 |
| False | True | False | True | True | False | True | 0.92 | 0.08 |
| False | True | False | True | True | False | False | 0.51 | 0.49 |
| False | True | False | True | False | True | True | 0.83 | 0.17 |
| False | True | False | True | False | True | False | 0.08 | 0.92 |
| False | True | False | True | False | False | True | 0.32 | 0.68 |
| False | True | False | True | False | False | False | 0.82 | 0.18 |
| False | True | False | False | True | True | True | 0.64 | 0.36 |
| False | True | False | False | True | True | False | 0.1 | 0.9 |
| False | True | False | False | True | False | True | 0.53 | 0.47 |
| False | True | False | False | True | False | False | 0.02 | 0.98 |
| False | True | False | False | False | True | True | 0.75 | 0.25 |
| False | True | False | False | False | True | False | 0.37 | 0.63 |
| False | True | False | False | False | False | True | 0.8 | 0.2 |
| False | True | False | False | False | False | False | 0.6 | 0.4 |
| False | False | True | True | True | True | True | 0.74 | 0.26 |
| False | False | True | True | True | True | False | 0.84 | 0.16 |
| False | False | True | True | True | False | True | 0.06 | 0.94 |
| False | False | True | True | True | False | False | 0.53 | 0.47 |
| False | False | True | True | False | True | True | 0.18 | 0.82 |
| False | False | True | True | False | True | False | 0.06 | 0.94 |
| False | False | True | True | False | False | True | 0.82 | 0.18 |
| False | False | True | True | False | False | False | 0.47 | 0.53 |
| False | False | True | False | True | True | True | 0.65 | 0.35 |
| False | False | True | False | True | True | False | 0.77 | 0.23 |
| False | False | True | False | True | False | True | 0.9 | 0.1 |
| False | False | True | False | True | False | False | 0.92 | 0.08 |
| False | False | True | False | False | True | True | 0.32 | 0.68 |
| False | False | True | False | False | True | False | 0.07 | 0.93 |
| False | False | True | False | False | False | True | 0.01 | 0.99 |
| False | False | True | False | False | False | False | 0.14 | 0.86 |
| False | False | False | True | True | True | True | 0.43 | 0.57 |
| False | False | False | True | True | True | False | 0.82 | 0.18 |
| False | False | False | True | True | False | True | 0.4 | 0.6 |
| False | False | False | True | True | False | False | 0.9 | 0.1 |
| False | False | False | True | False | True | True | 0.33 | 0.67 |
| False | False | False | True | False | True | False | 0.63 | 0.37 |
| False | False | False | True | False | False | True | 0.79 | 0.21 |
| False | False | False | True | False | False | False | 0.7 | 0.3 |
| False | False | False | False | True | True | True | 0.69 | 0.31 |
| False | False | False | False | True | True | False | 0.27 | 0.73 |
| False | False | False | False | True | False | True | 0.12 | 0.88 |
| False | False | False | False | True | False | False | 0.73 | 0.27 |
| False | False | False | False | False | True | True | 0.83 | 0.17 |
| False | False | False | False | False | True | False | 0.47 | 0.53 |
| False | False | False | False | False | False | True | 0.28 | 0.72 |
| False | False | False | False | False | False | False | 0.98 | 0.02 |

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


| Door Doesn't Lock | Dirt | Incorrect Fan Speed | Incorrect Coolant Pressure | Compressor Failure | Incorrect Voltage | Incorrect Internal Temperature = True | Incorrect Internal Temperature = False |
|-------------------|------|---------------------|----------------------------|--------------------|-------------------|--------------------------------------|---------------------------------------|
| True | True | True | True | True | True | 0.03 | 0.97 |
| True | True | True | True | True | False | 0.39 | 0.61 |
| True | True | True | True | False | True | 0.55 | 0.45 |
| True | True | True | True | False | False | 0.95 | 0.05 |
| True | True | True | False | True | True | 0.71 | 0.29 |
| True | True | True | False | True | False | 0.48 | 0.52 |
| True | True | True | False | False | True | 0.37 | 0.63 |
| True | True | True | False | False | False | 0.13 | 0.87 |
| True | True | False | True | True | True | 0.09 | 0.91 |
| True | True | False | True | True | False | 0.25 | 0.75 |
| True | True | False | True | False | True | 0.07 | 0.93 |
| True | True | False | True | False | False | 0.92 | 0.08 |
| True | True | False | False | True | True | 0.43 | 0.57 |
| True | True | False | False | True | False | 0.84 | 0.16 |
| True | True | False | False | False | True | 0.51 | 0.49 |
| True | True | False | False | False | False | 0.36 | 0.64 |
| True | False | True | True | True | True | 0.32 | 0.68 |
| True | False | True | True | True | False | 0.22 | 0.78 |
| True | False | True | True | False | True | 0.47 | 0.53 |
| True | False | True | True | False | False | 0.19 | 0.81 |
| True | False | True | False | True | True | 0.76 | 0.24 |
| True | False | True | False | True | False | 0.98 | 0.02 |
| True | False | True | False | False | True | 0.03 | 0.97 |
| True | False | True | False | False | False | 0.12 | 0.88 |
| True | False | False | True | True | True | 0.34 | 0.66 |
| True | False | False | True | True | False | 0.84 | 0.16 |
| True | False | False | True | False | True | 0.62 | 0.38 |
| True | False | False | True | False | False | 0.32 | 0.68 |
| True | False | False | False | True | True | 0.31 | 0.69 |
| True | False | False | False | True | False | 0.62 | 0.38 |
| True | False | False | False | False | True | 0.98 | 0.02 |
| True | False | False | False | False | False | 0.53 | 0.47 |
| False | True | True | True | True | True | 0.39 | 0.61 |
| False | True | True | True | True | False | 0.86 | 0.14 |
| False | True | True | True | False | True | 0.82 | 0.18 |
| False | True | True | True | False | False | 0.38 | 0.62 |
| False | True | True | False | True | True | 0.78 | 0.22 |
| False | True | True | False | True | False | 0.34 | 0.66 |
| False | True | True | False | False | True | 0.95 | 0.05 |
| False | True | True | False | False | False | 0.98 | 0.02 |
| False | True | False | True | True | True | 0.81 | 0.19 |
| False | True | False | True | True | False | 0.22 | 0.78 |
| False | True | False | True | False | True | 0.17 | 0.83 |
| False | True | False | True | False | False | 0.7 | 0.3 |
| False | True | False | False | True | True | 0.64 | 0.36 |
| False | True | False | False | True | False | 0.2 | 0.8 |
| False | True | False | False | False | True | 0.24 | 0.76 |
| False | True | False | False | False | False | 0.45 | 0.55 |
| False | False | True | True | True | True | 0.99 | 0.01 |
| False | False | True | True | True | False | 0.24 | 0.76 |
| False | False | True | True | False | True | 0.03 | 0.97 |
| False | False | True | True | False | False | 0.13 | 0.87 |
| False | False | True | False | True | True | 0.06 | 0.94 |
| False | False | True | False | True | False | 0.56 | 0.44 |
| False | False | True | False | False | True | 0.69 | 0.31 |
| False | False | True | False | False | False | 0.53 | 0.47 |
| False | False | False | True | True | True | 0.98 | 0.02 |
| False | False | False | True | True | False | 0.99 | 0.01 |
| False | False | False | True | False | True | 0.95 | 0.05 |
| False | False | False | True | False | False | 0.36 | 0.64 |
| False | False | False | False | True | True | 0.78 | 0.22 |
| False | False | False | False | True | False | 0.45 | 0.55 |
| False | False | False | False | False | True | 0.5 | 0.5 |
| False | False | False | False | False | False | 0.1 | 0.9 |


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
