# Azure Python Specifics

The best practice to use MSI providers within different Azure Resource thus eliminating the need for Keys.

Example of using `azure_ad` with Azure OpenAI resource and `quart` application on [`@bp.before_request`](https://github.com/Azure-Samples/azure-search-openai-demo/blob/f6e8729a7215bbcb18d469eaf0bd18808dda64f9/app/backend/app.py#L181C1-L181C19) or [`before_app_serving`](https://github.com/pamelafox/chatgpt-quickstart/blob/a63156404a1cc0bb56b198d21f22300c02d2d93e/src/quartapp/chat.py#L11)
