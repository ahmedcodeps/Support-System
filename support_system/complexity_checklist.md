# Complexity Checklist

| Operation | Data Structure | Time Complexity |
|---|---|---|
| Add request | Dictionary + Set + Queue | O(1) average |
| Check duplicate ID | Set | O(1) average |
| Process next request | Queue | O(1) |
| Undo update | Stack | O(1) |
| Search by ID | Dictionary | O(1) average |
| Search by customer | List/Dictionary values | O(n) |
| Sort requests | Python sorted() | O(n log n) |
| Display replies recursively | List + Recursion | O(n) |

## Space Complexity

- Requests dictionary: O(n)
- Request ID set: O(n)
- Queue: O(n)
- Undo stack: O(n)
- Replies: O(n)
- Recursion call stack: O(n) in the worst case