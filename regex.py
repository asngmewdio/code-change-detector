import re

# regex pattern for detecting tags
tag_pattern = r"\/\/\s*(<>|[<>-])?\s*#WJ\s*\d{4}-\d{2}-\d{2}\s*(.*?)?\s*(\/\/.*)?"

# example files
base_file = '''static bool CanPasteComponents(const USceneComponent* RootComponent, bool bOverrideCanAttach = false, bool bPasteAsArchetypes = false, const FString* SourceData = nullptr);

static void PasteComponents(TArray<UActorComponent*>& OutPastedComponents, AActor* TargetActor, USceneComponent* TargetComponent = nullptr, const FString* SourceData = nullptr);'''

changed_file = '''static bool CanPasteComponents(const USceneComponent* RootComponent, bool bOverrideCanAttach = false, bool bPasteAsArchetypes = false, const FString* SourceData = nullptr);

static void PasteComponents(TArray<UActorComponent*>& OutPastedComponents, AActor* TargetActor, USceneComponent* TargetComponent = nullptr, const FString* SourceData = nullptr);

// < #WJ 2022-04-28 Added Copy equivalent
static bool CanCopyComponents(const TArray<UActorComponent*>& ComponentsToCopy);

static void CopyComponents(const TArray<UActorComponent*>& ComponentsToCopy, FString* DestinationData = nullptr);
// > #WJ 2022-04-28'''

# find all tags in the changed file
tags = re.findall(tag_pattern, changed_file, flags=re.MULTILINE)

# print the tags
for tag in tags:
    print(tag)
