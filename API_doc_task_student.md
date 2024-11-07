
# API Documention Of Task Student
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


## 2.post New School API
## Endpoint
**Method**: `POST`  
**URL**: `http://127.0.0.1:8000/schools/`

## Description
Creates a new school entry in the database, allowing the association of one or more departments.



## Input
The request body should be a JSON object containing the following fields:

```json
{
    "school_name": "varsha public School",
    "school_location": "Ayakkad",
    "department_ID": [
        1,
        9
    ],
    "is_active": true
}
```
### Fields
* school_name (string): The name of the school.
* school_location (string): The location of the school.
* department_ID (array of integers): An array of department IDs associated with the school.
* is_active (boolean): Indicates whether the school is active.
## Responses

### Success (201 Created)

Returns the details of the newly created school.


**Response Example**:

```json
{
    "school_name": "varsha public School",
    "school_ID": 9,
    "school_location": "Ayakkad",
    "department_ID": [
        1,
        9
    ],
    "is_active": true,
    "created_on": "2024-11-03T18:34:04.978193Z",
    "updated_on": "2024-11-03T18:34:04.978219Z"
}
```

### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 400         | School with the specific ID not found    | `{"error": "School with the specific id not found"}` |
| 500         | Internal server error                    | `{"error": "An unexpected error occurred"}`           |




## 3.Get School by ID API
 

## Endpoint
**Method**: `GET`  
**URL**: `http://127.0.0.1:8000/schools/{school_ID}/`

## Description
Retrieves the details of a specific school based on the provided school ID.



## Parameters
* school_ID (integer): The unique identifier for the school you want to retrieve.

## Responses

### Success (200 OK)
Returns the details of the school with the specified ID.


**Response Example**:

```json
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
}
```

### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 400         | School with the specific ID not found    | `{"error": "School with the specific id not found"}` |
| 500         | Internal server error                    | `{"error": "An unexpected error occurred"}`           |




## 4.Update School by ID API


## Endpoint
**Method**: `PUT`  
**URL**: `http://127.0.0.1:8000/schools/{school_ID}/`

## Description

Updates the details of a specific school based on the provided school ID.


## Parameters
* school_ID (integer): The unique identifier for the school you want to update.
## Input
The request body should be a JSON object containing the following fields:

```json
{
    "school_name": "Marry Matha HS School",
    "school_location": "Kochi",
    "department_ID": [
        5,
        29
    ],
    "is_active": true
}
```
### Fields
* school_name (string): The name of the school.
* school_location (string): The location of the school.
* department_ID (array of integers): An array of department IDs associated with the school.
* is_active (boolean): Indicates whether the school is active.

## Responses

### Success (200 OK)
Returns the updated details of the school.


**Response Example**:

```json
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
    "updated_on": "2024-11-03T19:04:16.453868Z"
}
```

### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 400         | School with the specific ID not found    | `{"error": "School with the specific id not found"}` |
| 404         | School with the specific ID not found	 error                    | `{"error": "School not found"}`
| 500         | Internal server error                    | `{"error": "An unexpected error occurred"}`           |




## 5.Get All Teachers Under a School


## Endpoint
**Method**: `GET`  
**URL**: `http://127.0.0.1:8000/schools/teacher/{school_ID}/`

## Description

Retrieves a list of all teachers associated with a specific school, identified by the school ID.


## Parameters
* school_ID (integer): The unique identifier for the school whose teachers you want to retrieve.
## Responses

### Success (200 OK)
Returns a JSON array containing details about each teacher associated with the specified school.


**Response Example**:

```json
[
    {
        "employee_id": 101,
        "name": "Meera Menon",
        "performance": 89.25,
        "school_ID": 8,
        "department_ID": [
            9
        ],
        "is_active": true,
        "created_on": "2024-10-24T12:11:30.554479Z",
        "updated_on": "2024-11-02T14:40:02.736559Z"
    },
    {
        "employee_id": 105,
        "name": "Lata Iyer",
        "performance": 65.88888888888889,
        "school_ID": 8,
        "department_ID": [
            5
        ],
        "is_active": true,
        "created_on": "2024-10-24T12:11:30.577330Z",
        "updated_on": "2024-11-02T14:40:02.778490Z"
    },
    {
        "employee_id": 109,
        "name": "Nandini Pillai",
        "performance": 75.0,
        "school_ID": 8,
        "department_ID": [
            5
        ],
        "is_active": true,
        "created_on": "2024-10-24T12:11:30.598672Z",
        "updated_on": "2024-11-02T14:40:02.820562Z"
    }
]
```

### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 400         | School with the specific ID not found    | `{"error": "School with the specific id not found"}` |
| 500         | Internal server error                    | `{"error": "An unexpected error occurred"}`           |



## Get All Students Under a School 


## Endpoint
**Method**: `GET`  
**URL**: `http://127.0.0.1:8000/schools/student/{school_ID}/`

## Description
Retrieves a list of all students associated with a specific school, identified by the school ID.



## Parameters
school_ID (integer): The unique identifier for the school whose students you want to retrieve.

## Responses

### Success (200 OK)
Returns a JSON array containing details about each student associated with the specified school.


**Response Example**:

```json
[
    {
        "roll_no": 14,
        "name": "Lavanya Krishnan",
        "chemistry": 75,
        "physics": 30,
        "maths": 85,
        "total_marks_field": 190,
        "percentage_field": 63.33333333333333,
        "teacher_id": 114,
        "department_ID": 5,
        "school_ID": 1,
        "is_active": true,
        "created_on": "2024-10-25T06:11:19.721654Z",
        "updated_on": "2024-11-02T15:32:32.749336Z"
    },
    {
        "roll_no": 22,
        "name": "Lakshmi Raghavan",
        "chemistry": 60,
        "physics": 65,
        "maths": 70,
        "total_marks_field": 195,
        "percentage_field": 65.0,
        "teacher_id": 106,
        "department_ID": 5,
        "school_ID": 1,
        "is_active": true,
        "created_on": "2024-10-25T06:11:19.766236Z",
        "updated_on": "2024-11-02T14:47:14.478511Z"
    }
]
```

### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 404         | No students found for the specified school	    | `{"error": "No students found for this school"}` |
| 500         | Internal server error                    | `{"error": "An unexpected error occurred"}`           |



## Get All Active Schools API


## Endpoint
**Method**: `GET`  
**URL**: `http://127.0.0.1:8000/schools/active/`

## Description
Retrieves a list of all schools that are currently marked as active.



## Parameters
This endpoint does not require any parameters or authentication headers.

## Responses

### Success (200 OK)
Returns a JSON array containing details about each active school.


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
        "updated_on": "2024-11-03T19:04:16.453868Z"
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
    },
    {
        "school_name": "St. Joseph's School",
        "school_ID": 3,
        "school_location": "Kollam",
        "department_ID": [
            3,
            10
        ],
        "is_active": true,
        "created_on": "2024-10-24T11:02:23.474195Z",
        "updated_on": "2024-10-31T15:42:22.597204Z"
    }
]
```

### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 400         | Invalid request for status filtering   | `{"error": "Invalid status. Use 'active' or 'inactive'."}` |
| 500         | Internal server error                    | `{"error": "An unexpected error occurred"}`           |



## Get All Inactive Schools API


## Endpoint
**Method**: `GET`  
**URL**: `http://127.0.0.1:8000/schools/inactive/`

## Description
Retrieves a list of all schools that are currently marked as inactive.



## Parameters
This endpoint does not require any parameters or authentication headers.

## Responses

### Success (200 OK)
Returns a JSON array containing details about each inactive school.


**Response Example**:

```json
[
    {
        "school_name": "Marry Matha HS School",
        "school_ID": 9,
        "school_location": "Kochi",
        "department_ID": [
            5,
            29
        ],
        "is_active": false,
        "created_on": "2024-11-03T18:34:04.978193Z",
        "updated_on": "2024-11-03T19:28:21.521919Z"
    }
]

```

### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 400         | Invalid request for status filtering   | `{"error": "Invalid status. Use 'active' or 'inactive'."}` |
| 500         | Internal server error                    | `{"error": "An unexpected error occurred"}`           |

---

# Department Module APIs

## Create New Department


## Endpoint
**Method**: `POST`  
**URL**: `http://127.0.0.1:8000/departments/`

## Description
The Create New Department API allows users to add a new department to the system.

## Input
```json
{
    "department_name": "hindi",
    "department_HOD": 120,
    "school_ID": 3,
    "is_active": true
}
```

## Responses

### Success (200 OK)
Success Response Example:

**Response Example**:

```json
{
    "message": "Record created successfully",
    "data": {
        "department_ID": 31,
        "department_HOD": 120,
        "department_name": "hindi",
        "created_on": "2024-11-03T19:32:45.117330Z",
        "updated_on": "2024-11-03T19:32:45.117355Z",
        "is_active": true
    }
}
```
*Error Response Example (Unique Constraint Violation):*
```json
{
    "error": "UNIQUE constraint failed: department_app_department_task.department_HOD_id"
}
```


### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 400         | Bad request, typically due to validation errors    | `{"error": "UNIQUE constraint failed: department_app_department_task.department_HOD_id"}` |
| 500         | Internal server error                    | `{"error": "An unexpected error occurred"}`           |


>* The department_HOD field must be unique; attempting to create a department with an already defined HOD will result in a unique constraint error.

>*  Ensure that all required fields are correctly filled out to avoid validation errors.

## Get All Departments API


## Endpoint
**Method**: `GET`  
**URL**: `http://127.0.0.1:8000/departments/`

## Description
The Get All Departments API retrieves a list of all departments from the system, providing essential information such as department ID, head of department (HOD), and status.



## Parameters
This endpoint does not require any parameters or authentication headers.

## Responses

### Success
Successful Response Example:


**Response Example**:

```json
[
    {
        "department_ID": 1,
        "department_HOD": 113,
        "department_name": "Mathematics",
        "created_on": "2024-10-24T11:33:53.228759Z",
        "updated_on": "2024-10-30T07:09:27.298669Z",
        "is_active": true
    },
    {
        "department_ID": 2,
        "department_HOD": 108,
        "department_name": "Science",
        "created_on": "2024-10-24T11:34:24.072701Z",
        "updated_on": "2024-10-30T07:09:23.233952Z",
        "is_active": true
    },
    {
        "department_ID": 3,
        "department_HOD": 112,
        "department_name": "Literature",
        "created_on": "2024-10-24T11:34:37.634507Z",
        "updated_on": "2024-10-30T07:09:18.096488Z",
        "is_active": true
    }
]
```

### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 404         | Not found, typically when there are no departments available    | `No specific error message returned` |
| 500         | Internal server error                    | `{"error": "An unexpected error occurred"}`           |



## Get Department By department_ID

## Endpoint
**Method**: `GET`  
**URL**: ` http://127.0.0.1:8000/departments/<department_id>/`

## Description
The Get Department by ID API retrieves details for a specific department using its unique department ID

## Parameters
This endpoint does not require any parameters or authentication headers.

## Responses

### Success (200 OK)
Returns a JSON array with details about each school.

**Response Example**:

```json
{
    "department_ID": 5,
    "department_HOD": 105,
    "department_name": "Arts",
    "created_on": "2024-10-24T11:34:58.929930Z",
    "updated_on": "2024-11-03T09:58:19.857179Z",
    "is_active": true
}
```

### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 404         | Department not found with given ID	    | `No specific error message returned` |



## Update Department by ID API


## Endpoint
**Method**: `PUT`  
**URL**: `http://127.0.0.1:8000/departments/<department_ID>/`

## Description
The Update Department by ID API allows you to update the details of a specific department using its unique department ID.

## Parameters
* department_ID (path parameter): The ID of the department you wish to update.
* Request Body (JSON):
    ```json
    {
    "department_HOD": 105,
    "department_name": "Arts"
    }
    ```


## Responses

### Success (200 OK)


**Response Example**:

```json
{
    "department_ID": 5,
    "department_HOD": 105,
    "department_name": "Arts",
    "created_on": "2024-10-24T11:34:58.929930Z",
    "updated_on": "2024-11-04T08:56:57.953928Z",
    "is_active": true
}
```

### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 404         | Not found, typically when the specified department ID does not exist     | `No specific error message returned ` |
| 500         | Internal server error                    | `{"error": "An unexpected error occurred"}`           |



## Get Teachers Under Department API


## Endpoint
**Method**: `GET`  
**URL**: `http://127.0.0.1:8000/departments/teacher/<department_ID>/`

## Description
The Get Teachers Under Department API retrieves a list of teachers associated with a specific department identified by its unique department ID. 

## Parameters
* department_ID (path parameter): The ID of the department for which you want to retrieve the associated teachers.
## Responses

### Success (200 OK)
Returns a JSON array with details about each school.

**Response Example**:

```json
[
    {
        "employee_id": 100,
        "name": "Arjun das",
        "performance": 76.33333333333333,
        "school_ID": 5,
        "department_ID": [5],
        "is_active": true,
        "created_on": "2024-10-24T12:11:30.548955Z",
        "updated_on": "2024-11-02T14:40:02.725907Z"
    },
    {
        "employee_id": 105,
        "name": "Lata Iyer",
        "performance": 65.88888888888889,
        "school_ID": 8,
        "department_ID": [5],
        "is_active": true,
        "created_on": "2024-10-24T12:11:30.577330Z",
        "updated_on": "2024-11-02T14:40:02.778490Z"
    },
    {
        "employee_id": 107,
        "name": "Deepa Ramesh",
        "performance": 96.0,
        "school_ID": 5,
        "department_ID": [5],
        "is_active": true,
        "created_on": "2024-10-24T12:11:30.588636Z",
        "updated_on": "2024-11-02T14:40:02.800388Z"
    }
]
```

### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 400         | Not found, typically when the specified department ID does not exist or no teachers are associated with it    | `No specific error message returned` |
| 500         | Internal server error                    | `{"error": "An unexpected error occurred"}`           |



## Get All Departments by School API


## Endpoint
**Method**: `GET`  
**URL**: `http://127.0.0.1:8000/departments/departments-by-school/<school_id>/`

## Description
The Get All Departments by School API retrieves a list of departments associated with a specified school ID.

## Parameters
* school_id (integer): The ID of the school whose departments you want to retrieve.

## Responses

### Success (200 OK)
Returns a JSON array with details about each school.

**Response Example**:

```json
[
    {
        "department_ID": 5,
        "department_HOD": 105,
        "department_name": "Arts",
        "created_on": "2024-10-24T11:34:58.929930Z",
        "updated_on": "2024-11-04T08:56:57.953928Z",
        "is_active": true
    },
    {
        "department_ID": 9,
        "department_HOD": 101,
        "department_name": "Economics",
        "created_on": "2024-10-24T11:35:51.489364Z",
        "updated_on": "2024-10-30T07:08:29.478224Z",
        "is_active": true
    }
]
```

### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 404         | School not found	    | `{"error": "School with the specific id not found"}` |
| 500         | Internal server error                    | `{"error": "An unexpected error occurred"}`           |



## Get All Active Departments API


## Endpoint
**Method**: `GET`  
**URL**: `http://127.0.0.1:8000/departments/active/`

## Description
The Get All Active Departments API retrieves a list of all active departments. This endpoint is useful for fetching departments that are currently operational.



## Parameters
This endpoint does not require any path or query parameters.


## Responses

### Success (200 OK)
Returns a JSON array with details about each school.

**Response Example**:

```json
[
    {
        "department_ID": 1,
        "department_HOD": 113,
        "department_name": "Mathematics",
        "created_on": "2024-10-24T11:33:53.228759Z",
        "updated_on": "2024-10-30T07:09:27.298669Z",
        "is_active": true
    },
    {
        "department_ID": 2,
        "department_HOD": 108,
        "department_name": "Science",
        "created_on": "2024-10-24T11:34:24.072701Z",
        "updated_on": "2024-10-30T07:09:23.233952Z",
        "is_active": true
    },
    {
        "department_ID": 3,
        "department_HOD": 112,
        "department_name": "Literature",
        "created_on": "2024-10-24T11:34:37.634507Z",
        "updated_on": "2024-10-30T07:09:18.096488Z",
        "is_active": true
    },
    {
        "department_ID": 4,
        "department_HOD": 109,
        "department_name": "History",
        "created_on": "2024-10-24T11:34:48.967032Z",
        "updated_on": "2024-10-30T07:09:12.987219Z",
        "is_active": true
    },
    {
        "department_ID": 5,
        "department_HOD": 105,
        "department_name": "Arts",
        "created_on": "2024-10-24T11:34:58.929930Z",
        "updated_on": "2024-11-04T08:56:57.953928Z",
        "is_active": true
    }
]
```

### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 400         | Invalid status provided	    | `{"error": "Invalid status provided"}` |
| 500         | Internal server error                    | `{"error": "An unexpected error occurred"}`           |



## Get All Inactive Departments API


## Endpoint
**Method**: `GET`  
**URL**: `http://127.0.0.1:8000/departments/inactive/`

## Description

The Get All Inactive Departments API retrieves a list of all departments that are marked as inactive. This endpoint is useful for viewing departments that are not currently operational.


## Parameters
This endpoint does not require any path or query parameters.


## Responses

### Success (200 OK)

**Response Example**:

```json
[
    {
        "department_ID": 6,
        "department_HOD": 110,
        "department_name": "Philosophy",
        "created_on": "2024-10-24T12:00:00.123456Z",
        "updated_on": "2024-11-04T09:10:45.789012Z",
        "is_active": false
    },
    {
        "department_ID": 7,
        "department_HOD": 114,
        "department_name": "Sociology",
        "created_on": "2024-10-25T09:30:45.987654Z",
        "updated_on": "2024-11-03T15:22:33.123456Z",
        "is_active": false
    }
]
```

### Error Responses

| Status Code | Description                              | Example                                         |
|-------------|------------------------------------------|-------------------------------------------------|
| 400         | Invalid status provided	    | `{"error": "Invalid status provided"}` |
| 404        | No inactive departments found	                    | `{"error": "No inactive departments found"}` 
| 500         | Internal server error                    | `{"error": "An unexpected error occurred"}`           |


# Teacher App APIs

## Create Teacher API

## Endpoint
**Method**: `POST`  
**URL**: `http://127.0.0.1:8000/teachers/`

## Description
The Create Teacher API allows the addition of a new teacher to the system with basic details such as name, school ID, and department ID(s).



## Request Body

| Parameter       | Type     | Description                         | Required |
|-----------------|----------|-------------------------------------|----------|
| `name`          | string   | Name of the teacher                 | Yes      |
| `school_ID`     | integer  | ID of the school associated         | Yes      |
| `department_ID` | array    | List of department IDs              | Yes      |
| `is_active`     | boolean  | Status of the teacher (default: true) | No      |

## Example Request Body:

```json
{
    "name": "raveena",
    "school_ID": 1,
    "department_ID": [5],
    "is_active": true
}
```
## Responses

### Success (201 Created)

**Response Example**:

```json
{
    "employee_id": 136,
    "name": "raveena",
    "performance": 0.0,
    "school_ID": 1,
    "department_ID": [
        5
    ],
    "is_active": true,
    "created_on": "2024-11-04T09:57:51.451688Z",
    "updated_on": "2024-11-04T09:57:51.451765Z"
}
```

### Error Responses

| Status Code | Description                                    | Example Error Message                    |
|-------------|------------------------------------------------|------------------------------------------|
| 400         | Bad request due to validation errors           | `{"error": "Required fields missing"}`   |
| 500         | Internal server error, usually due to unexpected issues | `{"error": "An unexpected error occurred"}` |



## Get All Teachers API


## Endpoint
**Method**: `GET`  
**URL**: `http://127.0.0.1:8000/teachers/`

## Description
Get all teachers in json format.



## Responses

### Success (200 OK)
Returns a list of all teachers along with their details.


**Response Example**:

```json
[
    {
        "employee_id": 100,
        "name": "Arjun das",
        "performance": 76.33333333333333,
        "school_ID": 5,
        "department_ID": [
            5
        ],
        "is_active": true,
        "created_on": "2024-10-24T12:11:30.548955Z",
        "updated_on": "2024-11-02T14:40:02.725907Z"
    },
    {
        "employee_id": 101,
        "name": "Meera Menon",
        "performance": 89.25,
        "school_ID": 8,
        "department_ID": [
            9
        ],
        "is_active": true,
        "created_on": "2024-10-24T12:11:30.554479Z",
        "updated_on": "2024-11-02T14:40:02.736559Z"
    },
    {
        "employee_id": 102,
        "name": "Ravi Pillai",
        "performance": 70.0,
        "school_ID": 6,
        "department_ID": [
            6
        ],
        "is_active": true,
        "created_on": "2024-10-24T12:11:30.560637Z",
        "updated_on": "2024-11-02T14:40:02.747295Z"
    }
]
```

### Error Responses

| Status Code | Description                                      | Example Error Message                        |
|-------------|--------------------------------------------------|----------------------------------------------|
| 500         | Internal server error, usually due to unexpected issues | `{"error": "An unexpected error occurred"}` |




## Get Teacher by ID

**Method:** `GET`  
**URL:** `http://127.0.0.1:8000/teachers/{employee_id}/`  
**Description:** Retrieve the details of a specific teacher by their ID.


## Parameters

| Parameter | Type    | Description                          | Required |
|-----------|---------|--------------------------------------|----------|
| employee_id       | integer | The unique identifier of the teacher | Yes      |

### Input
- No request body is required for this operation.

### Response
- **Success Code:** `200 OK`

#### Response Example (JSON Format)
```json
{
    "employee_id": 115,
    "name": "Dinesh K. Nair",
    "performance": 86.76190476190476,
    "school_ID": 1,
    "department_ID": [
        29
    ],
    "is_active": true,
    "created_on": "2024-10-24T12:11:30.625841Z",
    "updated_on": "2024-11-02T14:40:02.882615Z"
}
```
## Error Response

| Status Code | Description                                | Example Error Message                        |
|-------------|--------------------------------------------|----------------------------------------------|
| 400         | Bad request due to invalid ID              | {"error": "id not found"}                   |
| 500         | Internal server error, usually due to unexpected issues | {"error": "Unexpected error occurred"} |


