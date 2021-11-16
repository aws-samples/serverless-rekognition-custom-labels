# Security Notes

Please read these security recommentations before using this repository

## Non Production

This sample code is a non-production ready template.

## Security recommentations for Jupyter Notebooks

The notebooks included in this reposiroty can be run from a local computer. However, 
please consider the following suggestions when executing them from an Amazon Sagemaker
instance:

- Please provision notebook instances inside a Virtual Private Cloud in order to be able to access VPC-only resources such as Amazon EFS file systems, resources which cannot be accessed outside a VPC network.
- Ensure data stored on Machine Learning (ML) storage volumes attached to the notebook instances are encrypted to protect SageMaker data at rest.
- Notebook instances must not be publicly accessible.
- Please configure an interface VPC endpoint to access S3. VPC endpoints are powered by AWS PrivateLink, a technology that enables you to privately access S3 APIs through private IP addresses.

Follow https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-security.html for more information