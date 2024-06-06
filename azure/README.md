# Azure Python Specifics

The best practice to use MSI providers within different Azure Resources thus eliminating the need for Keys.

Example of using `azure_ad` with Azure OpenAI resource and `quart` application on [`@bp.before_request`](https://github.com/Azure-Samples/azure-search-openai-demo/blob/f6e8729a7215bbcb18d469eaf0bd18808dda64f9/app/backend/app.py#L181C1-L181C19) or [`before_app_serving`](https://github.com/pamelafox/chatgpt-quickstart/blob/a63156404a1cc0bb56b198d21f22300c02d2d93e/src/quartapp/chat.py#L11)

## Using Managed Service Identity (MSI)

Managed Service Identity (MSI) allows your applications to authenticate to Azure services without storing credentials in your code. This is a more secure and manageable way to handle authentication.

### Example: Using MSI with Azure Key Vault

## Using Azure SDKs

Azure provides a rich set of SDKs for various services. Here are some examples:

### Example: Using Azure Storage SDK


## Best Practices

1. **Use Environment Variables**: Store sensitive information like connection strings and keys in environment variables instead of hardcoding them in your code.
2. **Leverage Azure Key Vault**: Use Azure Key Vault to manage and access secrets securely.
3. **Use Managed Identities**: Whenever possible, use Managed Identities to authenticate to Azure services.
4. **Monitor and Log**: Implement logging and monitoring to keep track of your application's performance and issues.
5. **Follow Azure SDK Guidelines**: Follow the guidelines and best practices provided in the Azure SDK documentation for the specific services you are using.

By following these tips and best practices, you can build secure and efficient applications on Azure using Python.
