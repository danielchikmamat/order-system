# Event-Driven Order System (Learning Plan)

**Tech Stack:**
- Backend: Python + FastAPI
- Kafka client: confluent-kafka-python
- Broker: Kafka (or Redpanda for easier local setup)
- Database: PostgreSQL

---

# 1. Project Goal

Build a simplified **event-driven order processing system** to understand:
- Microservices architecture
- Event-driven communication using Kafka
- Async processing patterns
- Data consistency with eventual consistency

You will build a system where services do NOT call each other directly. Instead, they communicate through Kafka events.

---

# 2. System Overview

## Services
You will implement 4–5 small services:

1. **Order Service** (API entry point)
2. **Payment Service**
3. **Inventory Service**
4. **Shipping Service**
5. **Notification Service**

---

## Event Flow (Happy Path)

1. Client creates order → Order Service
2. Order Service publishes `order.created`
3. Payment Service consumes → processes payment
4. Publishes `payment.succeeded`
5. Inventory Service consumes → reserves stock
6. Publishes `inventory.reserved`
7. Shipping Service consumes → ships order
8. Publishes `order.shipped`
9. Notification Service listens to all events

---

# 3. Phase 0 — Setup Infrastructure

## 3.1 Local Environment
Use Docker Compose:
- Kafka or Redpanda
- PostgreSQL
- Kafka UI (optional)

### Tasks:
- [ ] Setup Docker Compose
- [ ] Run Kafka broker
- [ ] Run PostgreSQL
- [ ] Test Kafka producer/consumer locally

---

# 4. Phase 1 — Design Event Contracts

Define all events BEFORE coding services.

## Events

### order.created
```json
{
  "order_id": "uuid",
  "user_id": "uuid",
  "items": [
    {"product_id": "p1", "quantity": 2}
  ],
  "total_amount": 100.0
}
```

### payment.succeeded
```json
{
  "order_id": "uuid",
  "payment_id": "uuid",
  "status": "SUCCESS"
}
```

### inventory.reserved
```json
{
  "order_id": "uuid",
  "status": "RESERVED"
}
```

### order.shipped
```json
{
  "order_id": "uuid",
  "tracking_id": "uuid"
}
```

---

## Tasks:
- [ ] Define event schemas
- [ ] Create shared `schemas/` folder
- [ ] Decide topic naming convention

---

# 5. Phase 2 — Order Service (FastAPI + PostgreSQL)

## Responsibilities
- Accept order requests
- Store order in DB
- Publish `order.created` event

## API Endpoint
```
POST /orders
```

## DB Table
```
orders
- id (uuid)
- user_id
- status
- total_amount
- created_at
```

## Kafka Topics
- Produces: `order.created`

## Tasks:
- [ ] Setup FastAPI project
- [ ] Connect PostgreSQL
- [ ] Create order table
- [ ] Implement POST /orders
- [ ] Publish Kafka event

---

# 6. Phase 3 — Payment Service

## Responsibilities
- Consume `order.created`
- Simulate payment processing
- Publish result event

## Kafka
- Consume: `order.created`
- Produce: `payment.succeeded` or `payment.failed`

## DB Table
```
payments
- id
- order_id
- status
- created_at
```

## Tasks:
- [ ] Kafka consumer setup
- [ ] Payment simulation logic
- [ ] Store payment result
- [ ] Publish event

---

# 7. Phase 4 — Inventory Service

## Responsibilities
- Consume payment success
- Check stock
- Reserve items

## Kafka
- Consume: `payment.succeeded`
- Produce: `inventory.reserved` or `inventory.failed`

## DB Table
```
inventory
- product_id
- quantity
```

## Tasks:
- [ ] Implement stock check
- [ ] Deduct inventory
- [ ] Publish event

---

# 8. Phase 5 — Shipping Service

## Responsibilities
- Consume inventory reserved
- Create shipment
- Publish shipping event

## Kafka
- Consume: `inventory.reserved`
- Produce: `order.shipped`

## DB Table
```
shipments
- id
- order_id
- tracking_id
```

## Tasks:
- [ ] Create shipment record
- [ ] Generate tracking ID
- [ ] Publish event

---

# 9. Phase 6 — Notification Service

## Responsibilities
- Listen to all events
- Print or send notifications

## Kafka
- Subscribe to all topics

## Tasks:
- [ ] Create consumer
- [ ] Log notifications

---

# 10. Phase 7 — Kafka Setup (confluent-kafka-python)

## Producer Example
```python
from confluent_kafka import Producer

producer = Producer({"bootstrap.servers": "localhost:9092"})

producer.produce("order.created", key="order1", value="json_string")
producer.flush()
```

## Consumer Example
```python
from confluent_kafka import Consumer

consumer = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "payment-service",
    "auto.offset.reset": "earliest"
})

consumer.subscribe(["order.created"])

while True:
    msg = consumer.poll(1.0)
    if msg:
        print(msg.value().decode("utf-8"))
```

---

# 11. Phase 8 — Error Handling

## You must implement:
- Retry logic in consumers
- Dead Letter Queue (DLQ)
- Idempotency (avoid duplicate processing)

---

# 12. Phase 9 — Eventual Consistency

Understand:
- Data is NOT immediately consistent
- Each service updates its own DB
- Kafka ensures propagation

---

# 13. Phase 10 — Testing

## Manual Testing Flow
- Create order via API
- Watch Kafka events
- Confirm DB updates across services

## Tools
- Postman
- Kafka UI
- Logs

---

# 14. Suggested Folder Structure

```
order-system/
│
├── order-service/
├── payment-service/
├── inventory-service/
├── shipping-service/
├── notification-service/
│
├── shared/
│   ├── schemas/
│   ├── kafka/
│
├── docker-compose.yml
└── README.md
```

---

# 15. Advanced Improvements (After Basics)

- Add Redis caching
- Add authentication (JWT)
- Add observability (Prometheus + Grafana)
- Use Avro + Schema Registry
- Implement Saga pattern properly

---

# 16. Learning Outcome

By finishing this project, you will understand:
- Kafka-based event-driven systems
- Microservice communication patterns
- Async processing with Python
- Real-world backend architecture design

---

# 17. Final Advice

Do NOT try to build everything at once.

Build in this order:
1. Kafka setup
2. Order service
3. Payment service
4. Inventory service
5. Shipping service
6. Notification service

---

