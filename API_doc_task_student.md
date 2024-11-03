
## 1. Get All Schools API

## Endpoint
**Method**: `GET`  
**URL**: `http://127.0.0.1:8000/schools/`

## Description
Retrieves a list of all schools in the database along with associated information like location, department IDs, and active status.

## Parameters
This endpoint does not require any parameters or authentication headers.

## Responses

### Success (200 OK)
Returns a JSON array with details about each school.

**Response Example**:

```json
[
    {
        "school_name": "Marry Matha HS School",
        "school_ID": 1,
        "school_location": "Kochi",
        "department_ID": [
            5,
            29
        ],
        "is_active": true,
        "created_on": "2024-10-24T11:01:54.091090Z",
        "updated_on": "2024-10-31T15:42:18.013992Z"
    },
    {
        "school_name": "Bharatiya Vidya Bhavan",
        "school_ID": 2,
        "school_location": "Thiruvananthapuram",
        "department_ID": [
            8,
            9
        ],
        "is_active": true,
        "created_on": "2024-10-24T11:02:11.035017Z",
        "updated_on": "2024-10-31T15:42:20.609962Z"
    }
]
```

### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 400         | School with the specific ID not found    | `{"error": "School with the specific id not found"}` |
| 500         | Internal server error                    | `{"error": "An unexpected error occurred"}`           |
