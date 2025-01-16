# This file conains the structure of the code

We will discuss the flow of all the diffrent components. This project has the following components:

| Component | Description | file or folder |
| --- | --- |
| API | This component is responsible for handling all the API requests. | wsgi.py |
| DataFetcher | This component is responsible for fetching the data from the API(Currenlty only the API from KamerVragen). | DataFetcher |
| Inference | This component is responsible for the inference with a large language model. | Inference |
| Ingester | This component is responsible for ingesting the data into the database. | Ingester |
| Modules | This component is responsible for the modules that are used in the project. | Modules |
| Querier | This component is responsible for querying documents from the database. | Querier |

Each component contains an readme file that explains the structure of the component. and the purpose of the component.