Feature: Type-Checking

  Scenario Outline: Type-Checking `<Python Source>` using `<Type Checker>`
    Given the Python source `<Python Source>`
    When running `<Type Checker>`
    Then type-checking should <Type Checks>

    Examples: Type Safety
      | Python Source                     | Type Checks | Notes                                                           |
      | type_safety/safe.py               | pass        | Types match for function inputs and outputs                     |
      | type_safety/safe_invalid.py       | fail        | Types mismatch for function inputs                              |
      | type_safety/unsafe_unannotated.py | fail        | No type information provided (PEP-484 requires this to succeed) |
      | type_safety/unsafe_func.py        | fail        | Function parameter of different type (TypeScript allows this)   |
      | type_safety/unsafe_any.py         | fail        | Unnecessary use of any (PEP-484 requires this to succeed)       |

    Examples: Null Safety
      | Python Source                              | Type Checks | Notes                                  |
      | null_safety/safe.py                        | pass        | All null-checks performed              |
      | null_safety/safe_invalid_write_none.py     | fail        | Non-optional variable assigned None    |
      | null_safety/safe_invalid_unchecked_read.py | fail        | Unchecked reading of optional variable |

    Examples: Exception Safety
      | Python Source                    | Type Checks | Notes                                  |
      | exception_safety/safe.py         | pass        | Both success/failure cases account for |
      | exception_safety/safe_invalid.py | fail        | Failure case not accounted for         |

    Examples: Exhaustiveness
      | Python Source                       | Type Checks | Notes                                              |
      | exhaustiveness/safe.py              | pass        | Match accounts for all possible enum values        |
      | exhaustiveness/safe_invalid.py      | fail        | Match does not account for all possible enum value |
      | exhaustiveness/safe_pair_invalid.py | fail        | Match does not account for all possible enum value |

    Examples: Encapsulation
      | Python Source                 | Type Checks | Notes                   |
      | encapsulation/safe_invalid.py | fail        | Private member accessed |

    Examples: Recursive Type
      | Python Source          | Type Checks | Notes                        |
      | recursive_type/json.py | pass        | JSON is an example of a type |
