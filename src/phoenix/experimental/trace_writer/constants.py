SPAN_DATAFRAME_TYPES = {
    'name': 'object',
    'span_kind': 'object',
    'parent_id': 'object',
    'start_time': 'datetime64[ns, UTC]',
    'end_time': 'datetime64[ns, UTC]',
    'status_code': 'object',
    'status_message': 'object',
    'events': 'object',
    'conversation': 'object',
    'context.trace_id': 'object',
    'context.span_id': 'object',
    'attributes.llm.output_messages': 'object',
    'attributes.llm.token_count.prompt': 'float64',
    'attributes.llm.model_name': 'object',
    'attributes.llm.input_messages': 'object',
    'attributes.llm.token_count.total': 'float64',
    'attributes.llm.invocation_parameters': 'object',
    'attributes.llm.token_count.completion': 'float64',
    'attributes.input.value': 'object',
    'attributes.input.mime_type': 'object',
    'attributes.output.value': 'object',
    'attributes.output.mime_type': 'object',
    'attributes.__computed__.latency_ms': 'float64',
    'attributes.__computed__.error_count': 'int64',
    'attributes.__computed__.cumulative_token_count.total': 'float64',
    'attributes.__computed__.cumulative_token_count.prompt': 'float64',
    'attributes.__computed__.cumulative_token_count.completion': 'float64',
    'attributes.retrieval.documents': 'object'
 }

# mapping from pandas to DataBricks SQL
SQL_TYPE_MAP = {
    'object': 'STRING',
    'float64': 'DOUBLE',
    'datetime64[ns, UTC]': 'TIMESTAMP',
    'int64': 'INT'
}